# Copyright 2025 Subteno (https://www.subteno.com).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    has_automatic_clear_on_click = fields.Boolean(
        string="Auto clear notification",
        default=True,
        help=(
            "If True, automatically clear the notification from mail box when clicking on it. "
            'Else, use "Mark as read" to clear the notification.'
        ),
    )
