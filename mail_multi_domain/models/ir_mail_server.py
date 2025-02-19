# Copyright 2025 Subteno (<https://www.subteno.com>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields


class IrMailServer(models.Model):
    _inherit = "ir.mail_server"

    force_alias_domain = fields.Char(
        string="Alias domain",
    )

    _sql_constraints = [
        ("unique_force_alias_domain", "UNIQUE(force_alias_domain, active)", "Force Alias Domain should be unique"),
    ]
