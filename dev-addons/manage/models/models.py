# -*- coding: utf-8 -*-

from odoo import models, fields, api


class task(models.Model):
    _name = 'manage.task' # module_name.model_name
    _description = 'manage.task'

#fields on DB
    name = fields.Char(string="Nombre", required=True, help="Escribe tu nombre") # task name and label is "nombre"
    # under field.char can be added more attributes like: readonly=True, required=True and help="help here".
    description = fields.Text(string="Descripción") # task description and label is "descripción"
    creation_date = fields.Date(string="Fecha de creación", default=fields.Date.today) # task creation date and label is "fecha de creación"
    start_date = fields.Date(string="Fecha de inicio") # task start date and label is "fecha de inicio"
    end_date = fields.Date(string="Fecha de fin") # task end date and label is "fecha de fin"
    is_paused = fields.Boolean(string="Pausada") # task is paused and label is "pausada"
    # many to one relation is a internal relation between two models what translate to consult the sprint of a task
    sprint = fields.Many2one('manage.sprint', string="Sprint") # task sprint and label is "sprint"
    # atribute: relation is the name of the table that will be created to store the relation
    # column1 and column2 are the names of the columns that will be created in the table to store the relation
    technology = fields.Many2many(comodel_name='manage.technology', string="Tecnología", relation='technologies_task', column1='task_id', column2='technology_id') # task technology and label is "tecnología"

class sprint(models.Model):
    _name = 'manage.sprint' # module_name.model_name
    _description = 'manage.sprint'
    
    name = fields.Char(string="Nombre", required=True, help="Escribe tu nombre") # sprint name and label is "nombre"
    description = fields.Text(string="Descripción") # sprint description and label is "descripción"
    start_date = fields.Date(string="Fecha de creación", default=fields.Date.today) # sprint creation date and label is "fecha de creación"
    end_date = fields.Date(string="Fecha de fin") # sprint end date and label is "fecha de fin"
    
    # one to many relation is a internal relation between two models what translate to consult all the tasks of a sprint
    # codemodel_name is the name of the model to be related
    # inverse_name is the name of the field in the related model
    # string is the label of the relation
    task = fields.One2many(comodel_name="manage.task", inverse_name='sprint', string="Tareas")
    
class technology(models.Model):
    _name = 'manage.technology'
    _description = 'manage.technology'
    
    name = fields.Char(string="Nombre", help="Escribe el nombre de la tecnología")
    description = fields.Text(string="Descripción")
    # can be binary, however it is recommended to use the Image field (which exists since version 16).
    #where max_width and max_height are the maximum dimensions of the image
    photo = fields.Image(max_width=300, max_height=300, string="Foto")
    task = fields.Many2many(comodel_name='manage.task', string="Tareas", relation='technologies_task', column1='technology_id', column2='task_id')
    