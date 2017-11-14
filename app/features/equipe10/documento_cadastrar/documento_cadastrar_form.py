from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired

class CadastrarDocumentoForm(Form):
    documento_tipo = TextAreaField('Tipo')
    documento_desc = TextAreaField('Descrição')
    file = FileField('Foto do Usuário', validators=[])