# Copyright 2024 Subteno IT
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    allowed_variant_ids = fields.Many2many(string="Allowed variants", comodel_name="product.template.attribute.value")

    # Overide
    def _get_matrix(self, product_template):
        """Return the matrix of the given product, updated with current SOLines quantities.

        :param product.template product_template:
        :return: matrix to display
        :rtype dict:
        """

        def has_ptavs(line, sorted_attr_ids):
            # TODO instead of sorting on ids, use odoo-defined order for matrix ?
            ptav = line.product_template_attribute_value_ids.ids
            pnav = line.product_no_variant_attribute_value_ids.ids
            pav = pnav + ptav
            pav.sort()
            return pav == sorted_attr_ids

        matrix = product_template._get_template_matrix(
            company_id=self.company_id,
            currency_id=self.currency_id,
            display_extra_price=True,
            # ! EDITED
            allowed_variant_ids=self.allowed_variant_ids.filtered(lambda l: l.product_tmpl_id.id == product_template.id),
        )
        if self.order_line:
            lines = matrix["matrix"]
            order_lines = self.order_line.filtered(lambda line: line.product_template_id == product_template)
            for line in lines:
                for cell in line:
                    if not cell.get("name", False):
                        line = order_lines.filtered(lambda line: has_ptavs(line, cell["ptav_ids"]))
                        if line:
                            cell.update({"qty": sum(line.mapped("product_uom_qty"))})
        return matrix
