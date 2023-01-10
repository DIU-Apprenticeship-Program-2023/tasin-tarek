from odoo import fields, models


class School(models.Model):
    _name = 'school.section'
    _description = 'school'

    name = fields.Char('Section')
    code = fields.Char('Section Code')