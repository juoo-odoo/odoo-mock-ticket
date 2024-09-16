from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # on sale order confirmation {state == 'sale'}.
    # for each product sold, set the product's {last_sale_price} to the {price_unit} of the sale order, specific to each {partner}
    # @api.model
    def write(self, vals):
        if vals.get('state') == 'sale':
            partner_id = self.partner_id.id
            for order in self.order_line:
                product_id = order.product_id.id
                price = order.price_unit
                
                # check if relation already exists in our DB
                partner_product_relation = self.env['lpsp.partner_product'].search([
                    ('product_id', '=', product_id),
                    ('partner_id', '=', partner_id)
                ], limit=1)

                # if it does, just update existing relation
                if partner_product_relation:
                    # print('Price found for partner: ', self.partner_id.id, ' and product', order.product_id.id, ' with price', price)
                    # print(partner_product_relation)
                    partner_product_relation.last_sale_price = price
                    # partner_product_relation.write({'last_sale_price': price})
                else: # create new relation
                    self.env['lpsp.partner_product'].create({ 
                        'partner_id': partner_id,
                        'product_id': product_id,
                        'last_sale_price': price,
                    })
        return super().write(vals)


    # Note -- Does not work. Why
    # @api.onchange('state') 
    # def _on_successful_sale_order(self):
    #     print('sale order hello')
    #     # import ipdb; ipdb.set_trace()
    #     for record in self:
    #         if record.state == 'sale':
    #             for order in self.order_line:
    #                 order.product_id.last_sale_price = order.price_unit