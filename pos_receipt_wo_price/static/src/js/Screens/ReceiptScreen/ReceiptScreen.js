/** @odoo-module **/
/**
 * Copyright 2022 Subteno (https://www.subteno.com).
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
 **/

const { useRef } = owl.hooks;
const ReceiptScreen = require("point_of_sale.ReceiptScreen");
const Registries = require("point_of_sale.Registries");

const ReceiptScreenWithoutPrice = (ReceiptScreen) =>
	class extends ReceiptScreen {
		constructor() {
			super(...arguments);
			this.orderReceiptWithoutPrice = useRef("order-receipt-without-price");
		}

		/**
		 * Print the receipt without price automatically if the printer is set else asks for printing in a popup.
		 */
		async _printReceiptWithoutPrice() {
			if (this.env.pos.proxy.printer) {
				await this.env.pos.proxy.printer.print_receipt(this.orderReceiptWithoutPrice.el.outerHTML);
			} else {
				return await this._printWeb();
			}
		}

		/**
		 * @Override
		 * Catch the moment the receipt with price is print in order to print the receipt without price before.
		 */
		async handleAutoPrint() {
			if (this._shouldAutoPrint()) {
				if (this.currentOrder.ticket_without_price) {
					await this.printReceiptWithoutPrice();
				}
				await this.printReceipt();
				if (this.currentOrder._printed && this._shouldCloseImmediately()) {
					this.whenClosing();
				}
			}
		}

		/**
		 * In cas there is no printer set on the PoS. Switch the views to display the receipt without price to print
		 * it using the Odoo standard methods.
		 */
		async printReceiptWithoutPrice() {
			let $receiptWithoutPrice = $("#receipt-without-price");
			let $receiptWithPrice = $("#receipt-with-price");
			this._switchReceipts($receiptWithoutPrice, $receiptWithPrice);
			await this._printReceiptWithoutPrice().then((r) =>
				this._switchReceipts($receiptWithPrice, $receiptWithoutPrice)
			);
		}

		/**
		 * Switch the receipt showed.
		 */
		_switchReceipts(receipt_1, receipt_2) {
			receipt_1.addClass("pos-receipt-container");
			receipt_1.css("display", "block");
			receipt_2.removeClass("pos-receipt-container");
			receipt_2.css("display", "none");
		}
	};

Registries.Component.extend(ReceiptScreen, ReceiptScreenWithoutPrice);

return ReceiptScreen;
