# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Consulta, Medico, Paciente
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    consultas = Consulta.query.all()
    # return {
    #    'consultas': consultas # 'consultas'
    #}
    return render_template('index.html', consultas=consultas)


@main.route('/nova', methods=['GET', 'POST'])
def nova_consulta():

    if request.method == 'POST':

        paciente = request.form['paciente']
        #data = request.form['data']
        #descricao = request.form['descricao']

        paciente = Paciente(
            nome=paciente
            # paciente=paciente,
            #data=data,
            #descricao=descricao
        )

        db.session.add(paciente)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise Exception('Erro ao salvar paciente')

        return redirect(url_for('main.index'))

    return render_template('nova.html')


@main.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    if request.method == 'POST':
        consulta.paciente = request.form['paciente']
        consulta.data = request.form['data']
        consulta.descricao = request.form['descricao']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('editar.html', consulta=consulta)


@main.route('/deletar/<int:id>')
def deletar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    db.session.delete(consulta)
    db.session.commit()
    return redirect(url_for('main.index'))