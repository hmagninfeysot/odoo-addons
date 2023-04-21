from odoo import models, fields


class hr_leave_allocation(models.Model):
    _inherit = 'hr.leave.allocation'

    negative_allocation = fields.Boolean(related="holiday_status_id.negative_allocation", store=True, string="Autorized negative allocation")

    _sql_constraints = [
        ('duration_check', "CHECK ( number_of_days >= 0 OR negative_allocation = True )", "The number of days must be greater than 0 if negative allocation is not authorized."),
    ]
