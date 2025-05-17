{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Tools',
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'summary': 'Real Estate Management', 
    'description': """
        Nuevo Modulo de Gestion de Inmuebles.
    """,   
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menu.xml',
    ],
}