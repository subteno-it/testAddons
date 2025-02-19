/** @odoo-module **/
/**
 * Copyright 2022 Subteno (https://www.subteno.com).
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
 **/

const { useRef } = owl.hooks;
const { nextFrame } = require("point_of_sale.utils");
const AbstractReceiptScreen = require("point_of_sale.AbstractReceiptScreen");
const Registries = require("point_of_sale.Registries");

const AbstractReceiptScreenWithoutPrice = (AbstractReceiptScreen) =>
	class extends AbstractReceiptScreen {
		constructor() {
			super(...arguments);
			this.orderReceiptWithoutPrice = useRef("order-receipt-without-price");
		}

		async _printReceiptWithoutTicket() {
			if (this.env.pos.proxy.printer) {
				const printResult = await this.env.pos.proxy.printer.print_receipt(
					this.orderReceiptWithoutPrice.el.outerHTML
				);
				if (printResult.successful) {
					return true;
				} else {
					const { confirmed } = await this.showPopup("ConfirmPopup", {
						title: printResult.message.title,
						body: "Do you want to print using the web printer?",
					});
					if (confirmed) {
						// We want to call the _printWeb when the popup is fully gone
						// from the screen which happens after the next animation frame.
						await nextFrame();
						return await this._printWeb();
					}
					return false;
				}
			} else {
				return await this._printWeb();
			}
		}
	};

Registries.Component.extend(AbstractReceiptScreen, AbstractReceiptScreenWithoutPrice);

return AbstractReceiptScreen;
