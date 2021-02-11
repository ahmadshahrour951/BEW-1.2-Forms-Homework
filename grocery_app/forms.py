from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryStore


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField(u'Title', validators=[DataRequired()])
    address = StringField(u'Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


def store_query():
    return GroceryStore.query


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""
    name = StringField('Name', validators=[
                       DataRequired(), Length(min=3, max=40)])
    price = FloatField('Price')
    category = SelectField('Category', choices=[('PRODUCE', 'Produce'), ('DELI', 'Deli'), (
        'BAKERY', 'Bakery'), ('PANTRY', 'Pantry'), ('FROZEN', 'Frozen'), ('OTHER', 'Other')])
    photo_url = StringField('Photo Url', validators=[DataRequired(), URL()])
    store = QuerySelectField(
        'Store Name', query_factory=store_query)
    submit = SubmitField('Submit')
