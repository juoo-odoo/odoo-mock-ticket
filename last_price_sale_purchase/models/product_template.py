from odoo import api, fields, models

class ProductProduct(models.Model):
    _inherit = 'product.template'
    
    last_cost_price = fields.Float(readonly=True)
    last_sale_price = fields.Float(readonly=True)

# product.template is parent of product.product