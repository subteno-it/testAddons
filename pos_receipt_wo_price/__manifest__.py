# Copyright 2022 Subteno (https://www.subteno.com).
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Point of Sale - Receipt without price",
    "version": "17.0.0.0.0",
    "category": "Point of sale",
    "description": """Add a new configuration for the point of sale in order to generate receipt without price.""",
    "author": "Subteno",
    "website": "https://www.subteno.com",
    "depends": [
        "point_of_sale",
    ],
    "data": [
        "views/pos_config.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_receipt_wo_price/static/src/js/Screens/PaymentScreen/PaymentScreen.js",
            "pos_receipt_wo_price/static/src/js/Screens/ReceiptScreen/OrderReceiptWithoutPrice.js",
            "pos_receipt_wo_price/static/src/js/Screens/ReceiptScreen/ReceiptScreen.js",
            "pos_receipt_wo_price/static/src/js/Screens/TicketScreen/ControlButtons/ReprintReceiptButtonWithoutPrice.js",
            "pos_receipt_wo_price/static/src/js/Screens/TicketScreen/ReprintReceiptScreenWithoutPrice.js",
            "pos_receipt_wo_price/static/src/js/Screens/TicketScreen/TicketScreen.js",
            "pos_receipt_wo_price/static/src/js/models.js",
        ],
        "web.assets_qweb": [
            "pos_receipt_wo_price/static/src/**/*.xml",
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
    "price": 99.99,
    "currency": "EUR",
}
