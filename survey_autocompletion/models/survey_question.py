# Copyright 2025 Subteno (https://www.subteno.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SurveyQuestion(models.Model):
    _inherit = "survey.question"

    autocompleted_field_id = fields.Many2one(
        string="Field for autocomplete",
        comodel_name="ir.model.fields",
        domain="[('model_id', '=', autocompleted_model_id)]",
        help="Specifies the field in the reference model used for autocompletion.",
    )
    autocompleted_model_id = fields.Many2one(
        string="Reference Question Model",
        comodel_name="ir.model",
        related="autocompleted_question_id.reference_model_id",
        help="Technical field: Provides a relation to the model of the reference question used for autocompletion.",
    )
    autocompleted_question_id = fields.Many2one(
        string="Reference Question",
        comodel_name="survey.question",
        domain=(
            "[('survey_id', '=', survey_id), ('is_used_for_reference', '=', True), '|',"
            " ('sequence', '<', sequence), '&', ('sequence', '=', sequence), ('id', '<', id)]"
        ),
        help="Specifies the reference question to be used for autocompletion.",
    )
    category_id = fields.Many2one(
        string="Partner Category",
        comodel_name="res.partner.category",
        help="Field used to filter partner if reference model is res.partner",
    )
    is_autocompleted = fields.Boolean(
        string="Autocompleted ?",
        help="Indicates whether the survey question is set for autocompletion.",
    )
    is_used_for_reference = fields.Boolean(
        string="Used as Reference ?",
        help="Indicates whether the survey question is used as a reference.",
    )
    reference_field_id = fields.Many2one(
        string="Reference Field",
        comodel_name="ir.model.fields",
        domain="[('model_id', '=', reference_model_id)]",
        help="Specifies the field in the reference model to which the survey question is referring.",
    )
    reference_model = fields.Char(
        string="Reference Model Name",
        related="reference_model_id.model",
        help="Model name of the reference model.",
    )
    reference_model_id = fields.Many2one(
        string="Reference Model",
        comodel_name="ir.model",
        help="Specifies the model to which the survey question is referring.",
    )

    @api.constrains("is_used_for_reference", "is_autocompleted")
    def _check_autocomplete(self):
        """
        Constraint to check that a question cannot be both a reference and set for autocompletion.

        Raises:
            UserError: If a question is marked both as a reference and for autocompletion.
        """
        if self.filtered(lambda q: q.is_used_for_reference and q.is_autocompleted):
            raise UserError(_("A question cannot be a reference and autocompleted. (Not Implemented)"))
