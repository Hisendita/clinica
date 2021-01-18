# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class visitas_model(models.Model):
    _name = 'gestion_pacientes.visitas_model'
    _description = 'Gestion de visitas del paciente'

    paciente = fields.Many2one("gestion_pacientes.paciente_model", string="Paciente")
    fecha = fields.Date(string="Fecha", required=True, help="Fecha de visita", default=datetime.today())
    detalle = fields.Html(string="Detalle", required=True, help="Detalle de la visita")