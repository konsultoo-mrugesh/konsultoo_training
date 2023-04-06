from odoo import models, fields, _

from odoo15.odoo import api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    name = fields.Char('Name')

    coupon_code_id = fields.Many2one('coupon.generator')
    #
    # @api.onchange('partner_id')
    # def _onchange_on_partner_id(self):
    #     if self.partner_id:
    #         self.coupon_code_id = sel
        # coupon_code = self.partner_id.child_ids.ids
        # if self.partner_id.child_ids:
        #     self.coupon_code_id = [(6, 0, coupon_code)]