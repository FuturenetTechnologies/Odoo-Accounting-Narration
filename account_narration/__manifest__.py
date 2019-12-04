# -*- coding: utf-8 -*-
{
    'name': 'Custom Accounting Module',
    'version': '11.1',
    'category': 'Invoicing',
    'author': 'Futurenet Technologies',    
    'description': """ Customized Accounting module and inherited the following details
    1. Narration column in Payment screen
    2. Internal notes in tree view - Invoice screen
    3. Cheque number and cheque date in Payment and Journal entry screen
    4. Vendor due list report
    5. Menu name changed - Receipts, Credit note and Debit note
    6. Cheque payment report
    7. Journal voucher report
       """,
    'depends': ['base','account'],
    'installable': True,
    'auto_install': False,
    'data' : [
             'views/report_layout.xml',
             'views/account_invoice_inherit.xml',
             'views/account_payment_inherit.xml',
             'wizard/account_invoice_wizard.xml',
             'wizard/invoice_due_report.xml',
              ],
    'qweb': [
            ],
    'price': 10,
    'currency': 'EUR'

}
