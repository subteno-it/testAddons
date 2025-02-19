/** @odoo-module **/
/**
 * Copyright 2022 Subteno (https://www.subteno.com).
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
 **/

const AbstractReceiptScreen = require("point_of_sale.AbstractReceiptScreen");
const Registries = require("point_of_sale.Registries");

const ReprintReceiptScreenWithoutPrice = (AbstractReceiptScreen) => {
	class ReprintReceiptScreenWithoutPrice extends AbstractReceiptScreen {
		mounted() {
			this.printReceipt();
		}

		confirm() {
			this.showScreen("TicketScreen", { reuseSavedUIState: false });
		}

		async printReceipt() {
			if (this.env.pos.proxy.printer && this.env.pos.config.iface_print_skip_screen) {
				let result = await this._printReceipt();
				if (result) this.showScreen("TicketScreen", { reuseSavedUIState: false });
			}
		}

		async tryReprint() {
			await this._printReceipt();
		}
	}

	ReprintReceiptScreenWithoutPrice.template = "ReprintReceiptScreenWithoutPrice";
	return ReprintReceiptScreenWithoutPrice;
};
Registries.Component.addByExtending(ReprintReceiptScreenWithoutPrice, AbstractReceiptScreen);

return ReprintReceiptScreenWithoutPrice;
