from odoo import api, fields, models, _


class AccountInvoiceInherit(models.Model):
    _inherit = "account.invoice"

    # FUNCTION TO CHANGE NAME FOR CREDIT AND DEBIT NOTE
    @api.multi
    def name_get(self):
        TYPES = {
            'out_invoice': _('Invoice'),
            'in_invoice': _('Vendor Bill'),
            'out_refund': _('Credit Note'),
            'in_refund': _('Vendor Debit note'),
        }
        result = []
        for inv in self:
            result.append((inv.id, "%s %s" % (inv.number or TYPES[inv.type], inv.name or '')))
        return result

    # FUNCTION FOR CALCULATING CHEQUE AMOUNT
    @api.one
    @api.depends('amount_total')
    def _get_cheque_amount(self):
        if self.amount_total:
            self.cheque_amount = self.amount_total

    # FUNCTION FOR CALCULATING CHEQUE DATE
    @api.one
    @api.depends('date_due')
    def _get_cheque_date(self):
        if self.date_due:
            self.cheque_date = self.date_due

    cheque_number = fields.Char("Cheque Number")
    cheque_amount = fields.Float("Cheque Amount", compute="_get_cheque_amount")
    cheque_date = fields.Date("Cheque Date", compute="_get_cheque_date")
    cheque_details = fields.Text("Cheque Details")   
    note = fields.Char("Notes")
    narration = fields.Char("Narration")
    number_ref = fields.Char("Number Ref")


class AccountMoveInherit(models.Model):
    _inherit = "account.move"
            
    cheque_number = fields.Char("Cheque Number")
    cheque_date = fields.Date("Cheque Date")
    cheque_narration = fields.Char("Cheque Narration")
