from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, IntegerField, EmailField
from wtforms import validators, EmailField
from wtforms.validators import DataRequired

class ZodiacoForm(Form):
    nombre= StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=3, max=10, message='El campo debe tener entre 3 y 10 caracteres')
    ]
    )
    apellidoP= StringField('Apellido Paterno',[
        validators.DataRequired(message='El campo es requerido')
    ]
    )
    apellidoM= StringField('Apellido Materno',[
        validators.DataRequired(message='El campo es requerido')
    ]
    )
    fechaN=StringField('Fecha de Nacimiento (año-mes-dia)',[
        validators.DataRequired(message='El campo es requerido')
    ]
    )

    sexo = RadioField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')], validators=[DataRequired()])