# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Lead(models.Model):
    _inherit = 'crm.lead'
#     _name = 'neuron.neuron'
#     _description = 'neuron.neuron'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
    def custom_button_method(self):
        link = 'https://integrator-neuron.systems/neuronodoo/handler/phone.php?'
        for record in self:
            link += 'user_id=' + str(record.user_id.id)
            link += '&user_name=' + str(record.user_id.name)
            link += '&entity_id=' + str(record.id)
            link += '&current_user_id=' + str(self.env.user.id)
            link += '&current_user_id=' + str(self.env.user.id)
            link += '&current_user_name=' + str(self.env.user.name)
            link += '&contact_name=' + str(record.contact_name)
        return {
            'type': 'ir.actions.act_url',
            'url': link,
        }

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
