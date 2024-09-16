from odoo import api, fields, models, Command

class Partner(models.Model):
    _inherit = 'res.partner'

    product_prices_ids = fields.One2many("lpsp.partner_product", "partner_id")