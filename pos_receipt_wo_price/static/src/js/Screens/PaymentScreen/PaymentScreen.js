/** @odoo-module **/
/**
 * Copyright 2022 Subteno (https://www.subteno.com).
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
 **/

const PaymentScreen = require("point_of_sale.PaymentScreen");
const Registries = require("point_of_sale.Registries");

const PaymentScreenWithoutPrice = (PaymentScreen) =>
	class extends PaymentScreen {
		/**
		 * Toggle if a receipt without price should be printed and had style to show that the button is active.
		 */
		toggleIsWithTicketWithoutPrice() {
			this.currentOrder.set_with_ticket_without_price(!this.currentOrder.is_with_ticket_without_price());
			this.render();
		}
	};

Registries.Component.extend(PaymentScreen, PaymentScreenWithoutPrice);

return PaymentScreen;
