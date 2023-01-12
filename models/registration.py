from odoo import fields, models


class School(models.Model):
    _name = 'school.registration'
    _description = 'school'

    section_id = fields.Many2one('school.section','Section')
    course_id = fields.Many2one('school.course','Course')
    teacher_id = fields.Many2one('school.teacher','Teacher')
    student_ids = fields.Many2many('school.student','registration_student_rel','registration_id','student_id','Student List')