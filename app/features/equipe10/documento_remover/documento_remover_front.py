from .documento_remover_negocio import DocumentoRemoverNegocio
from app import app
from ....utils.front_helper import *

@app.route('/documento/remover/<documento_id>', methods=['GET', 'POST'])
<<<<<<< HEAD
#@login_required
#@verifica_permissao
=======
@login_required
@verifica_permissao
>>>>>>> origin/master
def documento_desativar(documento_id):
    return DocumentoRemoverNegocio.exibir(documento_id)