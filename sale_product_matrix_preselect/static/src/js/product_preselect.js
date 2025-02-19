/** @odoo-module */

import { ProductTemplateAttributeLinePreselect } from "./product_template_attribute_line_preselect";
import { Product } from "@sale_product_configurator/js/product/product";

export class ProductPreselect extends Product {
	static components = { PTAL: ProductTemplateAttributeLinePreselect };
	static template = "ProductPreselect";
}
