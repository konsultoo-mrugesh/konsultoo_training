{
    'name': 'coupon genrator',
    'version': '15.0.1.1.0',
    'summary': 'coupon genrator information',
    'description': """Helps to show product information""",
    'category': 'Human Resources',
    'depends': ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/coupon_manager_group.xml',
        'reports/coupon_report.xml',
        'reports/coupon_report_template.xml',
        'views/coupon_genrator.xml',
        'views/coupon_master.xml',
        'views/res_partner_inherit.xml',
        'views/sale_order_inherit.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

