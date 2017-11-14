from .processo_cadastrar_form import CadastrarProcessoForm
from ....tables.equipe10.processo.processo_modelo import Processo
from ....utils.flash_errors import flash_errors

from flask import render_template, flash, redirect, url_for

class ProcessoCadastrarNegocio:

    def exibir():
        form = CadastrarProcessoForm()

        if form.validate_on_submit():

            processo = Processo()
            processo.tipo = form.processo_tipo.data
            processo.desc = form.processo_desc.data


            processo.salva()
            return redirect(url_for('processo_listar'))
        else:
            flash_errors(form)

        return render_template('processo_criar.html', form=form)