from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class BooksForm(FlaskForm):
    #id = IntegerField('ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    full_name = TextAreaField('AuthorFullName', validators=[DataRequired()])
    status = BooleanField('Shelf')
    # polska = IntegerField('Koszt')
