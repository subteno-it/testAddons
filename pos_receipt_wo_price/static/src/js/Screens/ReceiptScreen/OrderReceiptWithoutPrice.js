/** @odoo-module **/
/**
 * Copyright 2022 Subteno (https://www.subteno.com).
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
 **/

const PosComponent = require("point_of_sale.PosComponent");
const Registries = require("point_of_sale.Registries");

class OrderReceiptWithoutPrice extends PosComponent {
	constructor() {
		super(...arguments);
		this._receiptEnv = this.props.order.getOrderReceiptEnv();
	}

	/**
	 * Get the current receipt selected.
	 */
	get receipt() {
		return this.receiptEnv.receipt;
	}

	/**
	 * Get the lines of the order.
	 */
	get orderlines() {
		return this.receiptEnv.orderlines;
	}

	/**
	 * Get the environnement of the receipt such as the order, the PoS and so on.
	 */
	get receiptEnv() {
		return this._receiptEnv;
	}

	/**
	 * Propagates the order to generate the receipt.
	 */
	willUpdateProps(nextProps) {
		this._receiptEnv = nextProps.order.getOrderReceiptEnv();
	}
}

OrderReceiptWithoutPrice.template = "OrderReceiptWithoutPrice";

Registries.Component.add(OrderReceiptWithoutPrice);

return OrderReceiptWithoutPrice;
