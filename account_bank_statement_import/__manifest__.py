# -*- encoding: utf-8 -*-
{
    'name': 'Account Bank Statement Import',
    'category': 'Accounting',
    'version': '1.0',
    'author': 'ITGRUPO-COMPATIBLE-BO',
    'depends': ['account'],
    'description': """Generic Wizard to Import Bank Statements. Includes the import of files in .OFX format""",
    'data': [
        'account_bank_statement_import_view.xml',
        'account_import_tip_data.xml',
        'wizard/journal_creation.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': True,
}
