from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class BooksForm(FlaskForm):
    #id = IntegerField('ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    type = TextAreaField('Description', validators=[DataRequired()])
    # polska = IntegerField('Koszt')
