# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class paciente_model(models.Model):
    _name = 'gestion_pacientes.paciente_model'
    _description = 'Descripcion del paciente'

    name = fields.Char(string="Nombre", required=True, index=True, help="Nombre del paciente")
    surname = fields.Char(string="Apellidos", required=True,help="Apellidos del paciente")
    dni = fields.Char(string="DNI",required=True,size=9,help="DNI del paciente")
    telefono = fields.Integer(string="Telefono",size=9,help="Numero de telefono del paciente")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento",required=True,help="Fecha de nacimiento del paciente",default=datetime.today())
    email = fields.Char(string="e-mail",required=False,size=100,help="Email del paciente")
    foto = fields.Binary()
    
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100