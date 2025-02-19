/** @odoo-module */

import { ProductMatrixPreselectDialog } from "./product_matrix_preselect_dialog";
import { SaleOrderLineProductField } from "@sale/js/sale_product_field";
import { serializeDateTime } from "@web/core/l10n/dates";

import { patch } from "@web/core/utils/patch";

patch(SaleOrderLineProductField.prototype, {
	async _openGridConfigurator(edit = false, allowed_variant_ids = [], preselected = false) {
		if (this.props.preselection === true && preselected === false) return this._openProductPreselect();

		const saleOrderRecord = this.props.record.model.root;

		if (allowed_variant_ids.length) {
			await saleOrderRecord.update({
				allowed_variant_ids: [[6, 0, allowed_variant_ids]],
			});
		}

		return super._openGridConfigurator(edit);
	},

	async _openProductPreselect() {
		const saleOrderRecord = this.props.record.model.root;

		this.dialog.add(ProductMatrixPreselectDialog, {
			productTemplateId: this.props.record.data.product_template_id[0],
			ptavIds: this.props.record.data.product_template_attribute_value_ids.records.map((record) => record.resId),
			customAttributeValues: [],
			quantity: this.props.record.data.product_uom_qty,
			productUOMId: this.props.record.data.product_uom[0],
			companyId: saleOrderRecord.data.company_id[0],
			pricelistId: saleOrderRecord.data.pricelist_id[0],
			currencyId: this.props.record.data.currency_id[0],
			soDate: serializeDateTime(saleOrderRecord.data.date_order),
			edit: false,
			discard: () => {
				saleOrderRecord.data.order_line.delete(this.props.record);
			},
			_openGridConfigurator: this._openGridConfigurator.bind(this),
		});
	},

	async _onProductTemplateUpdate() {
		this.props.preselection = false;

		if (this.props.record.data.product_add_mode == "matrix") {
			const product = await this.orm.read(
				"product.template",
				[this.props.record.data.product_template_id[0]],
				["use_preselection"]
			);

			if (product.length && product[0].use_preselection) this.props.preselection = true;
		}

		super._onProductTemplateUpdate(...arguments);
	},

	async _openProductConfigurator(edit = false) {
		this.props.preselection = false;
		super._openProductConfigurator(...arguments);
	},
});
