from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class MainForm(FlaskForm):
    text = StringField('Your text', validators=[DataRequired()])
    remember = SubmitField('Remember')
    ask = SubmitField('Ask')
    code = SubmitField('Code')
    forget = SubmitField('Forget')


class ParametersForm(FlaskForm):
    inp = StringField('from', validators=[DataRequired()])
    out = StringField('to', validators=[DataRequired()])
    submit = SubmitField('Submit')
