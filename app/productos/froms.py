from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class NewProductForm(FlaskForm):
    nombre = StringField('Nombre del producto:')
    precio = IntegerField('Precio del producto: ')
    submit = SubmitField('Guardar')