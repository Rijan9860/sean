{
    'name': "Seed Entrepreneurs Association of Nepal (SEAN)",
    'version': '1.0',
    'summary': "Seed Entrepreneurs Association of Nepal (SEAN)",
    'description': """
    """,
    'author': "SunyaEK Computing",
    'website': "",
    'category': '', 
    'depends': [], 
    'data': [
        'security/custom_security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/customer_information_view.xml',
        'views/application_letter_view.xml'
    ],
    'demo': [
    ],
    'assets': {
        'web.assets_backend': [
            'sean/static/src/css/custom_style.css',
        ],
    },
    'installable': True,
    'application': True, 
    'auto_install': False,
    'license': 'LGPL-3', 
    'sequence': -120
}