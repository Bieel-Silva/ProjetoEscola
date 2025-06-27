from flask import Flask, jsonify, render_template, request, redirect, url_for
from app.database import get_db_connection, close_db_connection
from urllib.parse import quote as url_quote

app = Flask(__name__)

# Simulação de dados em memória (substitua por banco depois)
alunos = []
# Simulação de dados em memória para professores, turmas e disciplinas
professores = []
turmas = []
disciplinas = []
notas = []

@app.route('/')
def home():
    mensagem = "Bem-vindo ao Sistema de Gestão Escolar!"
    return render_template('index.html', mensagem=mensagem)

@app.route('/users')
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, email FROM users')
    users = cursor.fetchall()
    cursor.close()
    close_db_connection(conn)

    return jsonify([
        {"id": user[0], "username": user[1], "email": user[2]}
        for user in users
    ])

@app.route('/alunos')
def listar_alunos():
    return render_template('alunos.html', alunos=alunos)

@app.route('/alunos/novo', methods=['GET', 'POST'])
def novo_aluno():
    if request.method == 'POST':
        novo = {
            'id': len(alunos) + 1,
            'nome': request.form['nome'],
            'email': request.form['email']
        }
        alunos.append(novo)
        return redirect(url_for('listar_alunos'))
    return render_template('novo_aluno.html')

@app.route('/professores')
def listar_professores():
    return render_template('professores.html', professores=professores)

@app.route('/professores/novo', methods=['GET', 'POST'])
def novo_professor():
    if request.method == 'POST':
        novo = {
            'id': len(professores) + 1,
            'nome': request.form['nome'],
            'email': request.form['email']
        }
        professores.append(novo)
        return redirect(url_for('listar_professores'))
    return render_template('novo_professor.html')

@app.route('/turmas')
def listar_turmas():
    return render_template('turmas.html', turmas=turmas)

@app.route('/turmas/novo', methods=['GET', 'POST'])
def nova_turma():
    if request.method == 'POST':
        nova = {
            'id': len(turmas) + 1,
            'nome': request.form['nome']
        }
        turmas.append(nova)
        return redirect(url_for('listar_turmas'))
    return render_template('nova_turma.html')

@app.route('/disciplinas')
def listar_disciplinas():
    return render_template('disciplinas.html', disciplinas=disciplinas)

@app.route('/disciplinas/novo', methods=['GET', 'POST'])
def nova_disciplina():
    if request.method == 'POST':
        nova = {
            'id': len(disciplinas) + 1,
            'nome': request.form['nome']
        }
        disciplinas.append(nova)
        return redirect(url_for('listar_disciplinas'))
    return render_template('nova_disciplina.html')

@app.route('/notas')
def listar_notas():
    # Monta nomes para exibição
    notas_exibicao = []
    for nota in notas:
        aluno_nome = next((a['nome'] for a in alunos if a['id'] == nota['aluno_id']), 'Desconhecido')
        disciplina_nome = next((d['nome'] for d in disciplinas if d['id'] == nota['disciplina_id']), 'Desconhecida')
        notas_exibicao.append({
            'id': nota['id'],
            'aluno_nome': aluno_nome,
            'disciplina_nome': disciplina_nome,
            'valor': nota['valor']
        })
    return render_template('notas.html', notas=notas_exibicao)

@app.route('/notas/novo', methods=['GET', 'POST'])
def nova_nota():
    if request.method == 'POST':
        nova = {
            'id': len(notas) + 1,
            'aluno_id': int(request.form['aluno_id']),
            'disciplina_id': int(request.form['disciplina_id']),
            'valor': float(request.form['valor'])
        }
        notas.append(nova)
        return redirect(url_for('listar_notas'))
    return render_template('nova_nota.html', alunos=alunos, disciplinas=disciplinas)

@app.route('/healthcheck')
def healthcheck():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)