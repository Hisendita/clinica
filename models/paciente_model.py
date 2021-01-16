# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError
import re

class paciente_model(models.Model):
    _name = 'gestion_pacientes.paciente_model'
    _description = 'Descripcion del paciente'

    name = fields.Char(string="Nombre", required=True, index=True, help="Nombre del paciente")
    surname = fields.Char(string="Apellidos", required=True,help="Apellidos del paciente")
    dni = fields.Char(string="DNI",required=True,size=9,help="DNI del paciente")
    telefono = fields.Integer(string="Telefono",size=9,help="Numero de telefono del paciente")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento",required=True,help="Fecha de nacimiento del paciente",default=datetime.today())
    email = fields.Char(string="e-mail",required=False,size=100,help="Email del paciente")
    ## foto = fields.Binary()
    num_visitas = fields.Integer(string="Numero de visitas")
    
    @api.constrains("dni")
    def _check_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = self.dni[-1]
        num = int(self.dni[:-1])
        if letras[num%23] != letra:
            raise ValidationError("Error. DNI invalido.")
    
    @api.constrains("email")
    def _check_email(self):
        common_mails = [
            "@gmail.com", "@gmail.es", "@hotmail.com", "@hotmail.es", "@yahoo.com", "@yahoo.es", "@isca.es"
        ]
        
