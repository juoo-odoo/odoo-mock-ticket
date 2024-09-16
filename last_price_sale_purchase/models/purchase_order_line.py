from odoo import fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    last_cost = fields.Float('Last Cost', related="product_id.last_cost_price", readonly=True)

