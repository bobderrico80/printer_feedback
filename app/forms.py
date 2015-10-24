from flask_wtf import Form
from wtforms import DecimalField, FileField, IntegerField, SelectField, StringField
from wtforms.validators import DataRequired, Email, NumberRange


class NewJobForm(Form):
    job_name = StringField(u'Job Name', validators=[DataRequired()])
    email = StringField(u'Email Address', validators=[DataRequired(), Email()])
    infill = IntegerField(u'Infill', validators=[DataRequired(), NumberRange(min=1, max=100)])
    shells = IntegerField(u'Shells', validators=[DataRequired()])
    layer_height = DecimalField(u'Layer Height', validators=[DataRequired()])
    temperature = DecimalField(u'Temperature', validators=[DataRequired()])
    extrude_speed = SelectField(u'Extrude Speed', choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')])
    print_speed = SelectField(u'Print Speed', choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')])
    stl_file = FileField(u'STL File')
