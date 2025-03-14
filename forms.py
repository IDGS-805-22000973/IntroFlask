from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, IntegerField, EmailField
from wtforms import validators, EmailField

class UserForm(Form):
    matricula= StringField('Matricula', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=3, max=10, message='El campo debe tener entre 3 y 10 caracteres')
    ]
    )
    nombre= StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido')
    ]
    )
    apellido= StringField('Apellido',[
        validators.DataRequired(message='El campo es requerido')
    ]
    )
    email=EmailField('Correo',[
        validators.DataRequired(message='Ingresa un correo valido')
    ]
    )
