from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    matriculas = relationship('Matricula', back_populates='aluno')

class Professor(Base):
    __tablename__ = 'professores'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    disciplinas = relationship('Disciplina', back_populates='professor')

class Disciplina(Base):
    __tablename__ = 'disciplinas'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    professor_id = Column(Integer, ForeignKey('professores.id'))
    professor = relationship('Professor', back_populates='disciplinas')
    turmas = relationship('Turma', back_populates='disciplina')

class Turma(Base):
    __tablename__ = 'turmas'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    disciplina_id = Column(Integer, ForeignKey('disciplinas.id'))
    disciplina = relationship('Disciplina', back_populates='turmas')
    matriculas = relationship('Matricula', back_populates='turma')

class Matricula(Base):
    __tablename__ = 'matriculas'
    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey('alunos.id'))
    turma_id = Column(Integer, ForeignKey('turmas.id'))
    aluno = relationship('Aluno', back_populates='matriculas')
    turma = relationship('Turma', back_populates='matriculas')
