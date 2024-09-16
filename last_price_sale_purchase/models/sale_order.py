from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # on sale order confirmation {state == 'sale'}.
    # for each product sold, set the product's {last_sale_price} to the {price_unit} of the sale orde
    # @api.model
    def write(self, vals):
        if vals.get('state') == 'sale':
            for order in self.order_line:
                order.product_id.last_sale_price = order.price_unit
        return super().write(vals)


    # Note -- Does not work. Why
    @api.onchange('state') 
    def _on_successful_sale_order(self):
        print('sale order hello')
        import ipdb; ipdb.set_trace()
        for record in self:
            if record.state == 'sale':
                for order in self.order_line:
                    order.product_id.last_sale_price = order.price_unit