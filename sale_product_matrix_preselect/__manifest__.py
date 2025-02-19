# Copyright 2024 Subteno (https://www.subteno.com).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "Sale Product Matrix Preselect",
    "version": "1.0",
    "category": "Sales/Sales",
    "description": """Add the possibility to preselect some variants before opening grid view on sales orders.""",
    "author": "Fassi Théo, Subteno",
    "website": "https://www.subteno.com/",
    "price": 99.99,
    "currency": "EUR",
    "depends": [
        "sale_product_matrix",
    ],
    "data": [
        "views/product_attribute_views.xml",
        "views/product_template_views.xml",
        "views/sale_order_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "sale_product_matrix_preselect/static/src/js/product_matrix_preselect_dialog.js",
            "sale_product_matrix_preselect/static/src/js/product_preselect.js",
            "sale_product_matrix_preselect/static/src/js/product_list_preselect.js",
            "sale_product_matrix_preselect/static/src/js/product_template_attribute_line_preselect.js",
            "sale_product_matrix_preselect/static/src/js/sale_product_field.js",
            "sale_product_matrix_preselect/static/src/xml/**/*",
        ],
    },
    "application": True,
    "installable": True,
    "license": "LGPL-3",
}
