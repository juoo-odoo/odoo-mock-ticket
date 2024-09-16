from odoo import api, fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    last_cost = fields.Float('Last Cost', compute="_product_cost_for_partner", readonly=True)

    @api.depends('order_partner_id', 'product_id')
    def _product_price_for_partner(self):
        for record in self:
            partner_product_relation = self.env['lpsp.partner_product'].search([
                ('product_id', '=', record.product_id.id),
                ('partner_id', '=', record.order_partner_id.id)
            ], limit=1)
            record.last_price = partner_product_relation['last_cost_price'] # if partner_product_relation else 0.0




