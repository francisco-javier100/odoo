# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = 'sale.order'

    commitment_date = fields.Datetime(string='Fecha de Entrega', required=False, default='', help='Este espacio es solo para definir la fecha de entrega de dicho pedido.')
