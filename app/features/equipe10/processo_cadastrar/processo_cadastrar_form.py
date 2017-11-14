from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class CadastrarProcessoForm(Form):
    processo_tipo = TextAreaField('Tipo')
    processo_desc = TextAreaField('Descrição')