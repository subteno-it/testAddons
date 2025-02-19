# Copyright 2025 Subteno (https://www.subteno.com).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "Survey Autocompletion",
    "version": "17.0.0.0",
    "category": "Custom",
    "description": """
        This module enhances the functionality of the Odoo Survey application by introducing autocompletion features.
        It allows survey questions to be marked as references and supports autocompletion based on these references.

        Key Features:
        - Mark survey questions as references for further use.
        - Configure autocompletion by associating questions with reference questions.
    """,
    "author": "Fassi Théo, Subteno",
    "website": "https://www.subteno.com/",
    "price": 99.99,
    "currency": "EUR",
    "depends": [
        "survey",
    ],
    "data": ["views/survey_question_views.xml", "views/survey_templates.xml"],
    "assets": {"survey.survey_assets": ["survey_autocompletion/static/src/js/survey_form.js"]},
    'images': ['static/description/banner.gif'],
    "application": True,
    "installable": True,
    "license": "LGPL-3",
}
