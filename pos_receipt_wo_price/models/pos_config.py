
# Copyright 2022 Subteno (https://www.subteno.com).
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    allow_receipts_without_price = fields.Boolean(
        string='Allow receipts without price',
        help='This feature adds a new button in the PoS to create receipts without price.', )
