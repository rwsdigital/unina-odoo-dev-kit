# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductBrand(models.Model):
    _name = 'product.brand'

    name = fields.Char("Nome Brand",help='Il Nome del Brand',required=True)

    _sql_constraints = [
        ('uniq_name',
         'unique(name)',
         'The name must be unique'),
    ]

class ProductSeason(models.Model):
    _name = 'product.season'

    name = fields.Char("Nome Stagione",help='Codice Stagione',size=4,required=True)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one("product.brand",string="Brand",help='Il Nome del Brand')
    season_id = fields.Many2one("product.season",string="Stagione",help='Codice Stagione')
