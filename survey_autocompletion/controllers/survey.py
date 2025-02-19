# Copyright 2025 Subteno (https://www.subteno.com).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo.http import request, route
from odoo.addons.survey.controllers.main import Survey


class SurveyInherit(Survey):

    @route(
        "/survey/<string:survey_token>/<int:question_id>/<string:query>",
        type="json",
        auth="public",
        website=True,
        sitemap=False,
    )
    def get_autocomplete_values(self, survey_token, question_id, query):
        """
        Get autocomplete values for a specified question in a survey.

        Args:
            survey_token (str): Token associated with the survey.
            question_id (int): Identifier of the question for which autocomplete values are requested.
            query (str): The user search query.

        Returns:
            list: List of dictionaries containing autocomplete values for the specified question.
        """

        # undefined is unused, but is required to keep the same signature as the original method.
        survey_sudo, undefined = self._fetch_from_access_token(survey_token, False)

        question = survey_sudo.question_ids.filtered(lambda q: q.id == question_id)

        if not question or not question.is_used_for_reference:
            return []

        domain = [(question.reference_field_id.name, "=ilike", query)]

        if question.reference_model_id.model == "res.partner" and question.category_id:
            domain += [("category_id", "=", question.category_id.id)]

        res_model = request.env[question.reference_model_id.model].sudo().search(domain)

        if not res_model:
            return []

        res_model = res_model[0] if len(res_model) > 1 else res_model

        autocompleted_questions = survey_sudo.question_ids.filtered(
            lambda q: q.is_autocompleted and q.autocompleted_question_id.id == question.id
        )

        return [
            {"id": question.id, "value": res_model[question.autocompleted_field_id.name]}
            for question in autocompleted_questions
        ]
