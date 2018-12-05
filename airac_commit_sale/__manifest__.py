# -*- coding: utf-8 -*-
{
    'name': "airac_commit_sale",

    'summary': """
        El campo es para definir el numero de Trabajo para el pedido realizado..""",

    'description': """
        Ventas 00
    """,

    'author': "Francisco J. G. D.",
    'website': "http://www.isma5.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_form.xml',
        'report_saleorder.xml'
    ],
}
