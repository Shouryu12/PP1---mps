from .processo_listar_negocio import ProcessoListarNegocio
from app import app
from ....utils.front_helper import *


@app.route('/processo', methods=['GET', 'POST'])
<<<<<<< HEAD
#@login_required
#@verifica_permissao
=======
@login_required
@verifica_permissao
>>>>>>> origin/master
def processo_listar():
    return ProcessoListarNegocio.exibir()