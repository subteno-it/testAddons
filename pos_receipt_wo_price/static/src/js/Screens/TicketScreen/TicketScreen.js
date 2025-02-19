/** @odoo-module **/
/**
 * Copyright 2022 Subteno (https://www.subteno.com).
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
 **/

const TicketScreen = require("point_of_sale.TicketScreen");
const Registries = require("point_of_sale.Registries");

const TicketScreenWithoutPrice = (TicketScreen) =>
	class extends TicketScreen {
		/**
		 * Control if a ticket without price should be automatically printed before the ticket with price.
		 */
		get allowTicketsWithoutPrice() {
			return this.env.pos.config.allow_receipts_without_price;
		}

		/**
		 * @Override
		 * Replace the Reprint screen name to ProductScreen in order to use standard button in the PoS screens.
		 */
		getStatus(order) {
			if (order.locked) {
				return this.env._t("Paid");
			} else {
				const screen = order.get_screen_data();
				if (screen.name === "ReprintReceiptScreenWithoutPrice") {
					screen.name = "ProductScreen";
				}
				return this._getOrderStates().get(this._getScreenToStatusMap()[screen.name]).text;
			}
		}
	};

Registries.Component.extend(TicketScreen, TicketScreenWithoutPrice);

return TicketScreenWithoutPrice;
