# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class paciente_model(models.Model):
    _name = 'gestion_pacientes.paciente_model'
    _description = 'Descripcion del paciente'

    name = fields.Char(string="Nombre", required=True, index=True, help="Nombre del paciente")
    surname = fields.Char(string="Apellidos", required=True,help="Apellidos del paciente")
    dni = fields.Char(string="DNI",required=True,size=9,help="DNI del paciente")
    telefono = fields.Char(string="Telefono",size=9,help="Numero de telefono del paciente")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento",required=True,help="Fecha de nacimiento del paciente")
    email = fields.Char(string="e-mail",required=False,size=100,help="Email del paciente")
    img = fields.Binary()
    num_visitas = fields.Integer(string="Numero de visitas", compute="num_visitas", store=True)
    id_historial = fields.One2many("gestion_pacientes.visitas_model", "paciente")

    def delete_historial(self):
        self.ensure_one()
        for registro in self.id_historial:
            registro.unlink()
        return True

    @api.constrains("dni")
    def _check_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = self.dni[-1]
        num = int(self.dni[:-1])
        if letras[num%23] != letra:
            raise ValidationError("Error. DNI invalido.")
    
    @api.depends("id_historial")
    def numero_visitas(self):
        self.numero_visitas = len(self.id_historial)