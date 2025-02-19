/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { ProductConfiguratorDialog } from "@sale_product_configurator/js/product_configurator_dialog/product_configurator_dialog";
import { Dialog } from "@web/core/dialog/dialog";
import { ProductListPreselect } from "./product_list_preselect";

export class ProductMatrixPreselectDialog extends ProductConfiguratorDialog {
	static components = { Dialog, ProductListPreselect };
	static template = "ProductMatrixPreselectDialog";
	static props = ["*"];

	setup() {
		super.setup(...arguments);

		this.title = _t("Preselect variants for your product");
	}

	/**
	 * Override
	 */
	async _updateProductTemplateSelectedPTAV(productTmplId, ptalId, ptavId, multiIdsAllowed) {
		const product = this._findProduct(productTmplId);
		let selectedIds = product.attribute_lines.find((ptal) => ptal.id === ptalId).selected_attribute_value_ids;

		const ptavID = parseInt(ptavId);
		if (!selectedIds.includes(ptavID)) {
			selectedIds.push(ptavID);
		} else {
			selectedIds = selectedIds.filter((ptav) => ptav !== ptavID);
		}

		product.attribute_lines.find((ptal) => ptal.id === ptalId).selected_attribute_value_ids = selectedIds;
	}

	/**
	 * Override
	 */
	async onConfirm() {
		const selectedVariants = this.state.products[0].attribute_lines.flatMap((e) => e.selected_attribute_value_ids);

		this.props.close();

		this.props._openGridConfigurator(false, selectedVariants, true);
	}
}
