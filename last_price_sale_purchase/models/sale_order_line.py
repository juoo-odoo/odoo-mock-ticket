from odoo import fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    last_price = fields.Float('Last Price', related="product_id.last_sale_price", readonly=True)
