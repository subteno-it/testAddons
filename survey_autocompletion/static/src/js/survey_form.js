/** @odoo-module alias=survey_autocompletion.survey_form **/
/**
    Copyright 2025 Subteno (https://www.subteno.com).
    License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
*/

import { _t } from "web.core";
import surveyForm from "survey.form";

surveyForm.include({
	/**
	 * Override of the method to autocomplete other fields on user input.
	 *
	 * @override
	 * @param {Event} event - The event triggering the method.
	 */
	_updateEnterButtonText: async function (event) {
		const $target = event.target;
		const isTextbox = event.type === "focusin" && $target.tagName.toLowerCase() === "textarea";
		const text = !isTextbox ? _t("or press Enter") : isMac ? _t("or press ⌘+Enter") : _t("or press CTRL+Enter");
		$("#enter-tooltip").text(text);

		// End of Override - Start autocompletion

		if ($target.dataset.autocomplete !== "True" || $target.value === "") return;

		const questionId = $target.closest("[id]").id;

		if (!questionId) return;

		const autocompleteValues = await this._rpc({
			route: `/survey/${this.options.surveyToken}/${questionId}/${$target.value}`,
		});

		for (const value of autocompleteValues) {
			const elem = $(`div[id=${value.id}] input`);

			if (elem.length === 0) continue;

			elem[0].value = value.value;
		}
	},
});
