# Copyright 2024 Subteno IT
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import itertools

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    use_preselection = fields.Boolean(
        string="Use Preselection ?",
        help="If checked, a wizard to preselect variants will open before the grid view."
    )

    # Overide
    def _get_template_matrix(self, **kwargs):
        self.ensure_one()
        company_id = kwargs.get('company_id', None) or self.company_id or self.env.company
        currency_id = kwargs.get('currency_id', None) or self.currency_id
        display_extra = kwargs.get('display_extra_price', False)
        # ! EDITED
        allowed_variant_ids = kwargs.get('allowed_variant_ids', None)
        attribute_lines = self.valid_product_template_attribute_line_ids
        Attrib = self.env['product.template.attribute.value']
        # ! EDITED
        first_line_attributes = attribute_lines[0].product_template_value_ids.filtered(lambda a: (a.id in allowed_variant_ids.ids) if allowed_variant_ids else True)._only_active()
        # ! EDITED
        attribute_ids_by_line = [line.product_template_value_ids.filtered(lambda a: (a.id in allowed_variant_ids.ids) if allowed_variant_ids else True)._only_active().ids for line in attribute_lines]

        header = [{"name": self.display_name}] + [
            attr._grid_header_cell(
                fro_currency=self.currency_id,
                to_currency=currency_id,
                company=company_id,
                display_extra=display_extra
            ) for attr in first_line_attributes]

        result = [[]]
        for pool in attribute_ids_by_line:
            result = [x + [y] for y in pool for x in result]
        args = [iter(result)] * len(first_line_attributes)
        rows = itertools.zip_longest(*args)

        matrix = []
        for row in rows:
            row_attributes = Attrib.browse(row[0][1:])
            row_header_cell = row_attributes._grid_header_cell(
                fro_currency=self.currency_id,
                to_currency=currency_id,
                company=company_id,
                display_extra=display_extra)
            result = [row_header_cell]

            for cell in row:
                combination = Attrib.browse(cell)
                is_possible_combination = self._is_combination_possible(combination)
                cell.sort()
                result.append({
                    "ptav_ids": cell,
                    "qty": 0,
                    "is_possible_combination": is_possible_combination
                })
            matrix.append(result)

        return {
            "header": header,
            "matrix": matrix,
        }
