from odoo import http
from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale


class AvataxWebsiteSale(WebsiteSale):
    @http.route(
        "/shop/payment", type="http", auth="public", website=True, sitemap=False
    )
    def shop_payment(self, **post):
        order = request.cart
        if order:
            order._avatax_compute_tax()
        return super().shop_payment(**post)
