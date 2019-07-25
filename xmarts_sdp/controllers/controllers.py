# -*- coding: utf-8 -*-
from odoo import http

# class XmartsSdp(http.Controller):
#     @http.route('/xmarts_sdp/xmarts_sdp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xmarts_sdp/xmarts_sdp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xmarts_sdp.listing', {
#             'root': '/xmarts_sdp/xmarts_sdp',
#             'objects': http.request.env['xmarts_sdp.xmarts_sdp'].search([]),
#         })

#     @http.route('/xmarts_sdp/xmarts_sdp/objects/<model("xmarts_sdp.xmarts_sdp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xmarts_sdp.object', {
#             'object': obj
#         })