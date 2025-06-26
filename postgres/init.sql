-- Tabela Professor
CREATE TABLE Professor (
  id_professor SERIAL PRIMARY KEY,
  nome_completo VARCHAR(255) NOT NULL,
  email VARCHAR(100) NOT NULL,
  telefone VARCHAR(20)
);

-- Tabela Turma
CREATE TABLE Turma (
  id_turma SERIAL PRIMARY KEY,
  nome_turma VARCHAR(50) NOT NULL,
  id_professor INT,
  horario VARCHAR(100),
  FOREIGN KEY (id_professor) REFERENCES Professor(id_professor) ON DELETE SET NULL
);

-- Tabela Aluno
CREATE TABLE Aluno (
  id_aluno SERIAL PRIMARY KEY,
  nome_completo VARCHAR(255) NOT NULL,
  data_nascimento DATE NOT NULL,
  id_turma INT,
  nome_responsavel VARCHAR(255),
  telefone_responsavel VARCHAR(20),
  email_responsavel VARCHAR(100),
  informacoes_adicionais TEXT,
  FOREIGN KEY (id_turma) REFERENCES Turma(id_turma) ON DELETE SET NULL
);

-- Tabela Pagamento
CREATE TABLE Pagamento (
  id_pagamento SERIAL PRIMARY KEY,
  id_aluno INT,
  data_pagamento DATE NOT NULL,
  valor_pago DECIMAL(10,2) NOT NULL,
  forma_pagamento VARCHAR(50),
  referencia VARCHAR(100),
  status VARCHAR(20),
  FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno) ON DELETE CASCADE
);

-- Tabela Presenca
CREATE TABLE Presenca (
  id_presenca SERIAL PRIMARY KEY,
  id_aluno INT,
  data_presenca DATE NOT NULL,
  presente BOOLEAN NOT NULL,
  FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno) ON DELETE CASCADE
);

-- Tabela Atividade
CREATE TABLE Atividade (
  id_atividade SERIAL PRIMARY KEY,
  descricao TEXT NOT NULL,
  data_realizacao DATE NOT NULL
);

-- Tabela Atividade_Aluno (relacionamento entre Atividade e Aluno)
CREATE TABLE Atividade_Aluno (
  id_atividade INT,
  id_aluno INT,
  PRIMARY KEY (id_atividade, id_aluno),
  FOREIGN KEY (id_atividade) REFERENCES Atividade(id_atividade) ON DELETE CASCADE,
  FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno) ON DELETE CASCADE
);

-- Tabela Usuario
CREATE TABLE Usuario (
  id_usuario SERIAL PRIMARY KEY,
  login VARCHAR(50) UNIQUE NOT NULL,
  senha VARCHAR(255) NOT NULL,
  nivel_acesso VARCHAR(20),
  id_professor INT,
  FOREIGN KEY (id_professor) REFERENCES Professor(id_professor) ON DELETE SET NULL
);

-- Tabela Disciplina
CREATE TABLE Disciplina (
  id_disciplina SERIAL PRIMARY KEY,
  nome_disciplina VARCHAR(100) NOT NULL
);

-- Tabela Nota (relaciona Aluno, Disciplina e valor da nota)
CREATE TABLE Nota (
  id_nota SERIAL PRIMARY KEY,
  id_aluno INT NOT NULL,
  id_disciplina INT NOT NULL,
  valor NUMERIC(4,2) NOT NULL,
  FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno) ON DELETE CASCADE,
  FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id_disciplina) ON DELETE CASCADE
);

INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone) VALUES
('A001', 'João Silva', 'Rua A', 'São Paulo', 'SP', '01000-000', 'Brasil', '11999999999'),
('A002', 'Maria Oliveira', 'Rua B', 'Rio de Janeiro', 'RJ', '21000-000', 'Brasil', '21999999999'),
('A003', 'Pedro Santos', 'Rua C', 'Salvador', 'BA', '40000-000', 'Brasil', '71999999999');
