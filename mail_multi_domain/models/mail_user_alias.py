# Copyright 2025 Subteno (<https://www.subteno.com>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields


class MailUserAlias(models.Model):
    _name = "mail.user.alias"
    _order = "id"

    name = fields.Char(
        string="Name",
        required=True,
    )
    email = fields.Char(
        string="Email",
        required=True,
    )
    alias_domain = fields.Char(
        string="Alias Domain",
        required=True,
    )
    user_id = fields.Many2one(
        comodel_name="res.users",
        string="User",
        required=True,
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.user.company_id.id,
    )
    signature_alias = fields.Html(
        string="Signature",
        default="",
    )

    _sql_constraints = [("email_uniq", "unique(email,alias_domain)", "Email should be unique!")]
