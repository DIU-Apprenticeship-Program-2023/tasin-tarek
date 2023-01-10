from odoo import fields, models

class School(models.Model):
    _name = 'school.student'
    _description = 'school'

    name = fields.Char('Name', required= True)
    email = fields.Char('Email')
    phone = fields.Char('Contact')
    birth_date = fields.Date('Birth of Date: ')
    gender = fields.Selection([('M','Male'),('F','Female')], 'Gender')