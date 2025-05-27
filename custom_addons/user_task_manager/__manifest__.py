{
    'name': 'User Task manager',
    'version': '1.0',
    'category': 'Productivity',
    'author': 'Jose Salas',
    'license': 'LGPL-3',
    'summary': 'Modulo para la gestion de tareas de usuario',
    'description': """
        Gestion de tareas de usuario.
        Este modulo permite a los usuarios crear, asignar y gestionar tareas de manera eficiente.   
    """,
    'depends': ['base'],
    'data': [
        'data/ir_model.xml',
        'security/groups.xml',
        'security/user_task_security.xml',
        'security/ir.model.access.csv',
        'views/user_task_views.xml',

    ],
    'application': True,
  'installable': True,  
    'assets': {
        'web.assets_backend': [
            'user_task_manager/static/src/css/task_kanban.css',
        ],
       
    },
}