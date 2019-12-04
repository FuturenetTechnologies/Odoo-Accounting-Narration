from odoo import api, fields, models, _


class ReportDueVendorInvoice(models.AbstractModel):
    _name = 'report.custom_account.report_due_vendor_invoices'

    @api.model
    def get_report_values(self, docids, data=None):
        if not data.get('form'):
            raise UserError(_("Form content is missing, this report cannot be printed."))

        print('\n---',data,'--data--\n')
        return {
            'data': data.get('form')
            }


class VendorListWizard(models.TransientModel):
    _name = 'vendor.list.wizard'
    _description = "Attendance Report Wizard"


    @api.multi
    def print_report(self):
        domain = []
        print('\n---',self._context,'--self._context--\n')
        print('\n---',self.env.user.company_id,'--self.env.user.company_id--\n')
        datas = self.env['account.invoice'].search([('id', 'in', self._context.get('active_ids'))])
        # company = self.env['res.company'].search([('id', '=', self.env.user.company_id)])
        res = {
            'invoices': datas.ids,
            'company_id': self.env.user.company_id.id,
            'domain':  self._context.get('active_domain')[0][2]
        }
        data = {
            'form': res,
        }
        print('\n---',self._context.get('active_ids'),'--self._context.get)--\n')
        print('\n---',data, res,'--datas--\n')
        return self.env.ref('custom_account.report_due_invoices').report_action([], data=data)