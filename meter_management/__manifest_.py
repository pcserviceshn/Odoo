{
    'name': 'Meter Management',
    'version': '1.0',
    'summary': 'Module for managing metered goods',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/meter_data_views.xml',
        'views/meter_definition_views.xml',
        'views/meter_type_views.xml',
        'data/meter_data_sequence.xml',
    ],
    'application': True,
}
