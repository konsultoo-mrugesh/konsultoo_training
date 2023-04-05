from odoo import models, fields, api, _


class CouponMaster(models.Model):
    _name = 'coupon.master'
    _description = 'coupon master description'

    _sql_constraints = [('name_uniq', 'UNIQUE (name)', 'Name must be unique.')]


    name = fields.Char(string='Name', size=8, required=True)
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')

    currency_id = fields.Many2one('res.currency', string='Currency')
    coupon_value = fields.Monetary('Coupon Value',currency_field='currency_id')

    coupon_generator_id = fields.Many2one('coupon.generator')
