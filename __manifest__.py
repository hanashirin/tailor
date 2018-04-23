
{
'name' : 'TAILORING',
    'version' : '1.1',
    'summary': 'Send Invoices and Track Payments',
    'sequence': 30,
    'description': """tailoring system   """,
    'category': 'Accounting',
    'website': 'https://www.netexsystems.com/',
    'depends' : ['base','sales_team'],
    'data': [
        'views/desgn.xml'
        ],

    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}