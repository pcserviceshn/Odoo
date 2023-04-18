from odoo import models, fields

class MeterDefinition(models.Model):
    _name = 'meter.definition'
    _description = 'Meter Definition'

    name = fields.Char('Name', required=True)
    meter_type_id = fields.Many2one('meter.type', string='Meter Type', required=True)

