from .processo_remover_negocio import ProcessoRemoverNegocio
from app import app
from ....utils.front_helper import *

@app.route('/processo/remover/<processo_id>', methods=['GET', 'POST'])
<<<<<<< HEAD
#@login_required
#@verifica_permissao
=======
@login_required
@verifica_permissao
>>>>>>> origin/master
def processo_desativar(processo_id):
    return ProcessoRemoverNegocio.exibir(processo_id)