from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Property Tag'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Tag name must be unique.'),
    ]