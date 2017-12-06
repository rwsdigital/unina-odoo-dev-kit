# -*- coding: utf-8 -*-
from odoo import http

# class ModaAttributes(http.Controller):
#     @http.route('/moda_attributes/moda_attributes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/moda_attributes/moda_attributes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('moda_attributes.listing', {
#             'root': '/moda_attributes/moda_attributes',
#             'objects': http.request.env['moda_attributes.moda_attributes'].search([]),
#         })

#     @http.route('/moda_attributes/moda_attributes/objects/<model("moda_attributes.moda_attributes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('moda_attributes.object', {
#             'object': obj
#         })