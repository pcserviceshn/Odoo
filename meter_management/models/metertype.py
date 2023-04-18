from odoo import models, fields

class MeterType(models.Model):
    _name = 'meter.type'
    _description = 'Meter Type'

    name = fields.Char('Name', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)

