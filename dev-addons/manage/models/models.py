# -*- coding: utf-8 -*-

from odoo import models, fields, api


class task(models.Model):
    _name = 'manage.task' # module_name.model_name
    _description = 'manage.task'

#fields on DB
    name = fields.Char() # task name
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
