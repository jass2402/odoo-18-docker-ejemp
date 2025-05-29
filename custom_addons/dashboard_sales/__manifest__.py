{
    'name': 'Dashboard de Ventas',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Dashboard para visualizar métricas de ventas',
    'description': """ Dashboard con KPI's de ventas, incluyendo total de ventas, número de pedidos y productos más vendidos. """,
    'author': 'Jose Salas',
    'depends': ['sale', 'base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/dashboard_sales_views.xml',
        
    ],
    'installable': True,
    'application': True,
}