from odoo import models, fields

class MeterData(models.Model):
    _name = 'meter.data'
    _description = 'Meter Data'

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    meter_id = fields.Many2one('meter.definition', string='Meter', required=True)
    last_read = fields.Float('Last Read', required=True)
    current_read = fields.Float('Current Read', required=True)
    consumption = fields.Float('Consumption', compute='_compute_consumption')
    date = fields.Date('Date', required=True, default=fields.Date.today())

    @api.depends('last_read', 'current_read')
    def _compute_consumption(self):
        for record in self:
            record.consumption = record.current_read - record.last_read

