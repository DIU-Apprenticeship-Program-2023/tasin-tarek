from odoo import fields, models


class School(models.Model):
    _name = 'school.teacher'
    _description = 'school'

    name = fields.Char('Teacher Name', required=True)
    email = fields.Char('Email', required=True)
    phone = fields.Char('Contact')
    birth_date = fields.Date('Birth of Date: ')
    gender = fields.Selection([('M', 'Male'), ('F', 'Female')], 'Gender')
    image = fields.Image('Image')