from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    # on RFQ sent confirmation {state == 'sent'}.
    # for each product line, set the product's {last_cost_price} to the {price_unit} of the purchase order
    def write(self, vals):
        if vals.get('state') == 'sent':
            for order in self.order_line:
                order.product_id.last_cost_price = order.price_unit
        return super().write(vals)
