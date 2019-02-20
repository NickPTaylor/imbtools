"""
Forms for report blueprint.
"""

from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange, InputRequired

IMB_MEMBERS = [(1, 'Nick Taylor'),
               (2, 'Jeremy Colwill'),
               (3, 'Anne Duffy')]


class ReportForm(FlaskForm):
    """
    Form for rota report submission.
    """
    name = SelectField('Name', choices=IMB_MEMBERS, coerce=int,
                       validators=[DataRequired()])
    th_pop = IntegerField('Tinsley House Population',
                          validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit Report')
