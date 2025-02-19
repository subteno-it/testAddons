# Copyright 2024 Subteno IT
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProductAttribute(models.Model):
    _inherit = 'product.attribute'

    preselect_all = fields.Boolean(
        string="Preselect All ?",
        help="If checked, all attributes will be checked by default on the preselection view."
    )
