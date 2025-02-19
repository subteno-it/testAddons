/** @odoo-module **/
/**
 * Copyright 2022 Subteno (https://www.subteno.com).
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
 **/

import models from "point_of_sale.models";

const _super_order = models.Order.prototype;

models.Order = models.Order.extend({
	initialize: function (attributes, options) {
		_super_order.initialize.apply(this, arguments);
		this.ticket_without_price = false;
	},

	set_with_ticket_without_price: function (ticket_without_price) {
		this.assert_editable();
		this.ticket_without_price = ticket_without_price;
	},

	is_with_ticket_without_price: function () {
		return this.ticket_without_price;
	},
});
