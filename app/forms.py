from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.csrf import CSRFProtect
from flask import Flask

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    csrf.init_app(app)


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

    email = StringField('Email', validators=[Email()])

    sub = StringField('Subject', validators=[DataRequired()])

    msg = TextAreaField('Message', validators=[DataRequired()])

    submitbtn = SubmitField("Submit")