from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    # on RFQ sent confirmation {state == 'sent'}.
    # for each product line, set the product's {last_cost_price} to the {price_unit} of the purchase order
    def write(self, vals):
        if vals.get('state') == 'sent':
            partner_id = self.partner_id.id
            for order in self.order_line:
                product_id = order.product_id.id
                price = order.price_unit

                partner_product_relation = self.env['lpsp.partner_product'].search([
                    ('product_id', '=', product_id),
                    ('partner_id', '=', partner_id)
                ], limit=1)

                if partner_product_relation:
                    partner_product_relation.write({'last_cost_price': price})
                else:
                    self.env['lpsp.partner_product'].create({
                        'partner_id': partner_id,
                        'product_id': product_id,
                        'last_cost_price': price,
                    })
        return super().write(vals)