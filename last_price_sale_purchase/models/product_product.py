from odoo import api, fields, models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    last_cost_price = fields.Float(readonly=True)
    last_sale_price = fields.Float(readonly=True)

    # @api.model
    def write(self, vals):
        template = self.product_tmpl_id
        print(self, vals)
        if vals.get('last_cost_price'):
            template.last_cost_price = vals.get('last_cost_price')
        if vals.get('last_sale_price'):
            template.last_sale_price = vals.get('last_sale_price')
        return super().write(vals)
    # @api.onchange('last_cost_price', 'last_sale_price')
    # def _update_product_template(self):
    #     print('helo', self)
    #     for record in self:
    #         template = record.product_tmpl_id
    #         template.last_cost_price = self.last_cost_price
    #         template.last_sale_price = self.last_sale_price
