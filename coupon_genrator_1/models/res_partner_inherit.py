from odoo import models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    name = fields.Char('Name')

    coupon_count = fields.Integer('Count Coupon',compute='compute_count')

    def compute_count(self):
        for record in self:
            record.coupon_count = self.env['coupon.generator'].search_count(
                [('customer_ids', '=', self.id)])

    def get_coupon(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Coupon',
            'view_mode': 'tree',
            'res_model': 'coupon.generator',
            'domain': [('customer_ids', '=', self.id)],
            'target': 'new',
            # 'context': "{'create': False}"
        }
