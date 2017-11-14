from .documento_listar_negocio import DocumentoListarNegocio
from app import app
from ....utils.front_helper import *


@app.route('/documento', methods=['GET', 'POST'])
<<<<<<< HEAD
#@login_required
#@verifica_permissao
=======
@login_required
@verifica_permissao
>>>>>>> origin/master
def documento_listar():
    return DocumentoListarNegocio.exibir()