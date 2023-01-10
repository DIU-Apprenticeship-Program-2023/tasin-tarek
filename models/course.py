from odoo import fields, models


class School(models.Model):
    _name = 'school.course'
    _description = 'school'

    name = fields.Char('Course Name', required = True)
    course_code = fields.Char('Course Code')