from odoo import api, fields, models

# Many2many table for storing relationships and cost/sale price between partner and product variants
class PartnerProduct(models.Model):
    _name = 'lpsp.partner_product'

    partner_id = fields.Many2one("res.partner")
    product_id = fields.Many2one("product.product")

    last_cost_price = fields.Float(readonly=True)
    last_sale_price = fields.Float(readonly=True)
