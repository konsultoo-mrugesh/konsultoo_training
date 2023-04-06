import uuid

from odoo import models, fields, api, _


class Coupon(models.Model):
    _name = 'coupon.generator'
    _description = 'coupon city description'
    _rec_name = 'number'


    name = fields.Char(string='Coupon Name')
    number = fields.Integer('Number of Coupons')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    customer_ids = fields.Many2many('res.partner', string='Customers')
    Coupon_ids = fields.One2many('coupon.master', 'coupon_generator_id', 'Coupons')
    total_value = fields.Monetary('Total Value', currency_field='currency_id', compute='_compute_coupon')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)


    # def create_coupon_master(self):
    #     for rec in self.Coupon_ids:
    #         self.Coupon_ids = [
    #             (0,0,{
    #                 'name': rec.name,
    #                 'start_date': rec.start_date,
    #                 'end_date': rec.end_date,
    #             })
    #         ]

    def create_coupon_master(self):
        for rec in range(1, self.number+1):
            self.Coupon_ids = [
                (0, 0, {
                    # 'name': self.name + str(rec),
                    'name': str(uuid.uuid4()).replace('-', '')[:8],
                    'start_date':self.start_date,
                    'end_date':self.end_date,
                })
            ]
            print('rec:::::::::::',rec)



        # for rec in self.Coupon_ids:
        #     self.Coupon_ids = [
        #         (0,0,{
        #             'name': rec.name,
        #             'start_date': rec.start_date,
        #             'end_date': rec.end_date,
        #         })
        #     ]


    @api.depends('Coupon_ids')
    def _compute_coupon(self):
        total_coupon = []
        self.total_value = 0
        for rec in self.Coupon_ids:
            total_coupon.append(rec.coupon_value)
        self.total_value = sum(total_coupon)

    # @api.depends('Coupon_ids')
    # def _compute_coupon(self):
    #     total_coupon = []
    #     self.total_value = 0
    #     for rec in self.Coupon_ids:
    #         total_w = rec.coupon_value
    #         if total_w:
    #             total_coupon.append(total_w)
    #     self.total_value = sum(total_coupon)

    # @api.depends('Coupon_ids')
    # def _compute_coupon(self):
    #     for rec in self:
    #         rec.total_value = sum(rec.Coupon_ids.mapped('coupon_value'))




