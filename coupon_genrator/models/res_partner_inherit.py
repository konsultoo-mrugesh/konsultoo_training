from odoo import models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    name = fields.Char('Name')