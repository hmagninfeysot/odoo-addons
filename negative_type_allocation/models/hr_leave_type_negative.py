from odoo import models, fields


class hr_leave_type_negative(models.Model):
    _inherit = 'hr.leave.type'

    negative_allocation = fields.Boolean(string="Autorized negative allocation")