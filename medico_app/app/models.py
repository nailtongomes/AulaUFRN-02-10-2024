# models.py
from datetime import datetime
import json
from . import db


class Medico(db.Model):

    __tablename__ = 'medicos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    crm = db.Column(db.String(10), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)

    # relacionamentos
    # consultas = db.relationship('Consulta', backref='medico', lazy=True)

    @property
    def serialize(self):
        return {
            'nome': self.nome,
            'crm': self.crm,
            'especialidade': self.especialidade
        }


# classe para pacientes
class Paciente(db.Model):

    __tablename__ = 'pacientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    # relacionamentos
    # consultas = db.relationship('Consulta', backref='paciente', lazy=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
        }


class Consulta(db.Model):

    __tablename__ = 'consultas'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=False, default=datetime.now)
    descricao = db.Column(db.Text, nullable=False)
    campo_coringa = db.Column(db.Text, nullable=False)

    # relacionamentos
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    # paciente = db.relationship('Paciente', backref='consultas')

    @property
    def selialize(self):
        return {
            'paciente': self.paciente,
            'data': self.data,
            'descricao': self.descricao,
            'campo_coringa': json.loads(self.campo_coringa)
        }
