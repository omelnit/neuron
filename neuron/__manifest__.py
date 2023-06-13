# -*- coding: utf-8 -*-
{
    'name': "Neuron",

    'summary': "Interactive Phone Script Assistant",

    # 'description': """
    #     The script assistant is a universal assistant in which you can program all the options for developing a conversation for your managers. A tool that leads the manager automatically to a deal with a client. It also determines at what stage you lose customers.
    # """,

    'author': "Neuron",
    'website': "https://neuron-systems.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/CRM',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'license': 'LGPL-3',
}
