# -*- coding: utf-8 -*-
{
    'name': "Moda Attributes",

    'summary': """
        Aggiunta dei campi Brand e Stagione ai Prodotti""",

    'description': """
        Aggiunta dei campi Brand e Stagione ai Prodotti
    """,

    'author': "RWSdigital",
    'website': "http://www.rwsdigital.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
