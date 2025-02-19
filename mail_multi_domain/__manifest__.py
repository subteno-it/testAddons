# See LICENSE file for full copyright and licensing details.
{
    "name": "Mail Multi Domain",
    "summary": "Multi-domain management in Odoo",
    "description": """
        Our multi-domain email module has been designed for companies that want to be able to send emails with different alias, domain name and signatures.
        Thanks to our module, you will be able to configure your SMTP mail server in order to pre-define the alias and the signature which will be used in specific cases thanks to the combination of parameters that we propose, all of which is detailed in the documentation.
    """,
    "author": "Subteno IT",
    "website": "https://www.subteno.com",
    "category": "Discuss",
    "version": "0.2",
    "depends": [
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/ir_mail_server.xml",
        "views/res_company.xml",
        "views/mail_user_alias.xml",
        "views/res_users.xml",
        "data/base.xml",
    ],
    "images": [
        "static/description/vignette_multi_mail.png",
    ],
    "price": 125,
    "currency": "EUR",
    "license": "LGPL-3",
}
