/** @odoo-module */

import { ProductPreselect } from "./product_preselect";
import { ProductList } from "@sale_product_configurator/js/product_list/product_list";

export class ProductListPreselect extends ProductList {
	static components = { ProductPreselect };
	static template = "productListPreselect";
}
