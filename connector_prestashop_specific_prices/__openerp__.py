# -*- coding: utf-8 -*-
# © 2017 FactorLibre - Hugo Santos <hugo.santos@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Prestashop: Manage Specific Prices with pricelists',
    'version': '8.0.1.0.0',
    'depends': [
        'connector_prestashop'
    ],
    'category': 'Sales Management',
    'author': 'Odoo Community Association (OCA),FactorLibre',
    'license': 'AGPL-3',
    'website': 'http://www.factorlibre.com',
    'data': [
        'security/ir.model.access.csv',
        'views/prestashop_specific_price_view.xml',
        'views/product_pricelist_item_view.xml'
    ],
    'installable': True,
    'application': False
}
