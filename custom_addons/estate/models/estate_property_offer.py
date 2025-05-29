from odoo import fields, models, api
from datetime import date, timedelta
from odoo.exceptions import ValidationError
class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Real Estate Property Offer'
    _order = 'price asc'

    price = fields.Float(string='Price', required=True)
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')],
        string='Status', copy=False
    )
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True, ondelete='cascade')
    validity = fields.Date(string='Validity', compute='_compute_validity', inverse='_inverse_validity')
    date_deadline = fields.Date(string='Deadline')

    @api.depends('date_deadline')
    def _compute_validity(self):
        for record in self:
            if record.date_deadline:
                record.validity = record.date_deadline - timedelta(days=7)
            else:
                record.validity = False

    def _inverse_validity(self):
        for record in self:
            if record.validity:
                record.date_deadline = record.validity + timedelta(days=7)

    @api.model
    def create(self, vals):
        if vals.get('property_id') and vals.get('price'):
            property = self.env['estate.property'].browse(vals['property_id'])
            if property.offer_ids and vals['price'] < min(property.offer_ids.mapped('price')):
                raise ValidationError("The offered price must be higher than the lowest existing offer.")
            property.state = 'offer_received'
        return super().create(vals)

    def action_accept(self):
        for record in self:
            record.status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
            record.property_id.state = 'offer_accepted'
            # Refuse other offers
            for offer in record.property_id.offer_ids:
                if offer != record:
                    offer.status = 'refused'
        return True

    def action_refuse(self):
        for record in self:
            record.status = 'refused'
            if not record.property_id.offer_ids.filtered(lambda o: o.status == 'accepted'):
                record.property_id.state = 'offer_received'
        return True