# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Negative type allocation',
    'version': '14.0.1.0.1',
    'category': '',
    'license': 'AGPL-3',
    'summary': 'Negative allocation allow on type leave',
    'description': """
Negative type allocation
=================

This module offers a follow-up of your condominiums:

* TODO: update this list

This module has been written by Honoré Magnin-Feysot from exnihilosolution <https://github.com/hmagninfeysot>.
    """,
    'author': 'Honoré Magnin-Feysot',
    'website': 'https://www.exnihilosolution.com/',
    'depends': [
        'hr_holidays',
        'base', 
        ],
    'data': [
        'views/views_hr_leave_type_negative.xml',
        ],
    'installable': True,
}
