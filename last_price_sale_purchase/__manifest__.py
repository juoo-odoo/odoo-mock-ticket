{
    'name': 'last_price_sale_purchase',
    'depends': [
        'product',
        'sale',
        'purchase'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order_views.xml',
        'views/sale_order_views.xml',
        # 'views/product_product_views.xml',
        # 'views/product_template_views.xml'
    ]
}