from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="postgres",
        database="escola",
        user="postgres",
        password="postgres"
    )
    return conn


def listar_alunos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM alunos;')
    alunos = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    novo_aluno = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
        (novo_aluno['aluno_id'], novo_aluno['nome'], novo_aluno.get('endereco'), novo_aluno.get('cidade'),
         novo_aluno.get('estado'), novo_aluno.get('cep'), novo_aluno.get('pais'), novo_aluno.get('telefone'))
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Aluno cadastrado com sucesso!'}), 201


@app.route('/turmas', methods=['GET'])
def listar_turmas():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM turma;')
    turmas = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(turmas)

@app.route('/turmas/<int:id_turma>', methods=['GET'])
def obter_turma(id_turma):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM turma WHERE id_turma = %s;', (id_turma,))
    turma = cur.fetchone()
    cur.close()
    conn.close()
    if turma:
        return jsonify(turma)
    return jsonify({'message': 'Turma não encontrada'}), 404

@app.route('/turmas', methods=['POST'])
def cadastrar_turma():
    nova_turma = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO turma (nome_turma, id_professor, horario) VALUES (%s, %s, %s)',
        (nova_turma['nome_turma'], nova_turma.get('id_professor'), nova_turma.get('horario'))
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Turma cadastrada com sucesso!'}), 201

@app.route('/turmas/<int:id_turma>', methods=['PUT'])
def atualizar_turma(id_turma):
    dados_turma = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE turma SET nome_turma = %s, id_professor = %s, horario = %s WHERE id_turma = %s',
        (dados_turma['nome_turma'], dados_turma.get('id_professor'), dados_turma.get('horario'), id_turma)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Turma atualizada com sucesso!'})

@app.route('/turmas/<int:id_turma>', methods=['DELETE'])
def deletar_turma(id_turma):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM turma WHERE id_turma = %s;', (id_turma,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Turma deletada com sucesso!'})


@app.route('/professores', methods=['GET'])
def listar_professores():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM professor;')
    professores = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(professores)

@app.route('/professores/<int:id_professor>', methods=['GET'])
def obter_professor(id_professor):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM professor WHERE id_professor = %s;', (id_professor,))
    professor = cur.fetchone()
    cur.close()
    conn.close()
    if professor:
        return jsonify(professor)
    return jsonify({'message': 'Professor não encontrado'}), 404

@app.route('/professores', methods=['POST'])
def cadastrar_professor():
    novo_professor = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO professor (nome_completo, email, telefone) VALUES (%s, %s, %s)',
        (novo_professor['nome_completo'], novo_professor.get('email'), novo_professor.get('telefone'))
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Professor cadastrado com sucesso!'}), 201

@app.route('/professores/<int:id_professor>', methods=['PUT'])
def atualizar_professor(id_professor):
    dados_professor = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE professor SET nome_completo = %s, email = %s, telefone = %s WHERE id_professor = %s',
        (dados_professor['nome_completo'], dados_professor.get('email'), dados_professor.get('telefone'), id_professor)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Professor atualizado com sucesso!'})

@app.route('/professores/<int:id_professor>', methods=['DELETE'])
def deletar_professor(id_professor):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM professor WHERE id_professor = %s;', (id_professor,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Professor deletado com sucesso!'})

# CRUD para Pagamento
@app.route('/pagamentos', methods=['GET'])
def listar_pagamentos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pagamento;')
    pagamentos = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(pagamentos)

@app.route('/pagamentos/<int:id_pagamento>', methods=['GET'])
def obter_pagamento(id_pagamento):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pagamento WHERE id_pagamento = %s;', (id_pagamento,))
    pagamento = cur.fetchone()
    cur.close()
    conn.close()
    if pagamento:
        return jsonify(pagamento)
    return jsonify({'message': 'Pagamento não encontrado'}), 404

@app.route('/pagamentos', methods=['POST'])
def cadastrar_pagamento():
    novo_pagamento = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO pagamento (id_aluno, data_pagamento, valor_pago, forma_pagamento, referencia, status) VALUES (%s, %s, %s, %s, %s, %s)',
        (novo_pagamento['id_aluno'], novo_pagamento['data_pagamento'], novo_pagamento['valor_pago'],
         novo_pagamento.get('forma_pagamento'), novo_pagamento.get('referencia'), novo_pagamento.get('status'))
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Pagamento cadastrado com sucesso!'}), 201

@app.route('/pagamentos/<int:id_pagamento>', methods=['PUT'])
def atualizar_pagamento(id_pagamento):
    dados_pagamento = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE pagamento SET id_aluno = %s, data_pagamento = %s, valor_pago = %s, forma_pagamento = %s, referencia = %s, status = %s WHERE id_pagamento = %s',
        (dados_pagamento['id_aluno'], dados_pagamento['data_pagamento'], dados_pagamento['valor_pago'],
         dados_pagamento.get('forma_pagamento'), dados_pagamento.get('referencia'), dados_pagamento.get('status'), id_pagamento)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Pagamento atualizado com sucesso!'})

@app.route('/pagamentos/<int:id_pagamento>', methods=['DELETE'])
def deletar_pagamento(id_pagamento):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM pagamento WHERE id_pagamento = %s;', (id_pagamento,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Pagamento deletado com sucesso!'})

# Continue o mesmo padrão para Presenca, Atividade, Atividade_Aluno e Usuario.