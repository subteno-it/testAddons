# Copyright 2024 Subteno (https://www.subteno.com).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).


from odoo import http
from odoo.addons.sale_product_configurator.controllers.main import ProductConfiguratorController
from odoo.http import request

class PreselectProductConfiguratorController(ProductConfiguratorController):

    def _get_product_information(
        self,
        product_template,
        combination,
        currency_id,
        so_date,
        quantity=1,
        product_uom_id=None,
        pricelist_id=None,
        parent_combination=None,
    ):

        res = super()._get_product_information(
            product_template,
            combination,
            currency_id,
            so_date,
            quantity,
            product_uom_id,
            pricelist_id,
            parent_combination,
        )

        if not product_template.use_preselection:
            return res

        for attribute_line in res["attribute_lines"]:
            attribute = request.env["product.attribute"].browse(attribute_line["attribute"]["id"])

            if not attribute.preselect_all:
                continue

            attribute_line["selected_attribute_value_ids"] = list(
                map(lambda l: l["id"], attribute_line["attribute_values"])
            )

        return res
