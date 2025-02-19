/** @odoo-module */

import { ProductTemplateAttributeLine } from "@sale_product_configurator/js/product_template_attribute_line/product_template_attribute_line";

export class ProductTemplateAttributeLinePreselect extends ProductTemplateAttributeLine {
	/**
	 * Override
	 */
	getPTAVTemplate() {
		switch (this.props.attribute.display_type) {
			case "color":
				// ! EDITED used Custom template
				return "Preselect.ptav-color";
			case "multi":
				return "saleProductConfigurator.ptav-multi";
			case "pills":
				// ! EDITED used Custom template
				return "Preselect.ptav-pills";
			case "radio":
				// ! EDITED used Custom template
				return "Preselect.ptav-pills";
			case "select":
				// ! EDITED used Custom template
				return "Preselect.ptav-pills";
		}
	}
}
