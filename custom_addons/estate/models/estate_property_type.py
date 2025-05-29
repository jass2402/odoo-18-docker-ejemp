from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'
    _order = 'sequence, name'

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10, help="Used to order property types")
    property_ids = fields.One2many('estate.property', 'property_type_id')
    description = fields.Text(help="Description of the property type")
       


