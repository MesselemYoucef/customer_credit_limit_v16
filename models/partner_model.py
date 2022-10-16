from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    credit_limit = fields.Float(String="Credit Limit")
