# Copyright 2025 Subteno (<https://www.subteno.com>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    force_alias_domain = fields.Char(
        string="Alias domain",
    )
