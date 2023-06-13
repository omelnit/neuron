# -*- coding: utf-8 -*-
# from odoo import http


# class Neuron(http.Controller):
#     @http.route('/neuron/neuron', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/neuron/neuron/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('neuron.listing', {
#             'root': '/neuron/neuron',
#             'objects': http.request.env['neuron.neuron'].search([]),
#         })

#     @http.route('/neuron/neuron/objects/<model("neuron.neuron"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('neuron.object', {
#             'object': obj
#         })
