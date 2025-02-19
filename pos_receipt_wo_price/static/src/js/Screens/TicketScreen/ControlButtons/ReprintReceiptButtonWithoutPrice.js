/** @odoo-module **/
/**
 * Copyright 2022 Subteno (https://www.subteno.com).
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
 **/

const { useListener } = require("web.custom_hooks");
const PosComponent = require("point_of_sale.PosComponent");
const Registries = require("point_of_sale.Registries");

class ReprintReceiptButtonWithoutPrice extends PosComponent {
	constructor() {
		super(...arguments);
		useListener("click", this._onClickWithoutPrice);
	}

	/**
	 * Display the Screen of the Reprint Receipt Screen Without Price when the user clicks on the "Print without
	 * price" button.
	 */
	async _onClickWithoutPrice() {
		if (!this.props.order) return;
		this.showScreen("ReprintReceiptScreenWithoutPrice", { order: this.props.order });
	}
}

ReprintReceiptButtonWithoutPrice.template = "ReprintReceiptButtonWithoutPrice";
Registries.Component.add(ReprintReceiptButtonWithoutPrice);

return ReprintReceiptButtonWithoutPrice;
