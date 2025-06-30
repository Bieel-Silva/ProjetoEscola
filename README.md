<<<<<<< HEAD
# Projeto Escola

Este projeto é um sistema de gerenciamento escolar desenvolvido em PostgreSQL. Ele contém a estrutura de tabelas e relacionamentos necessários para gerenciar professores, turmas, alunos, pagamentos, presenças, atividades, usuários, disciplinas e notas.

## Estrutura do Banco de Dados

O banco de dados é composto pelas seguintes tabelas:

### 1. **Professor**
Armazena informações sobre os professores.
- **Colunas**:
  - `id_professor`: Identificador único do professor (chave primária).
  - `nome_completo`: Nome completo do professor.
  - `email`: E-mail do professor.
  - `telefone`: Telefone do professor.

### 2. **Turma**
Relaciona turmas com professores.
- **Colunas**:
  - `id_turma`: Identificador único da turma (chave primária).
  - `nome_turma`: Nome da turma.
  - `id_professor`: Identificador do professor responsável (chave estrangeira).
  - `horario`: Horário da turma.

### 3. **Aluno**
Armazena informações sobre os alunos.
- **Colunas**:
  - `id_aluno`: Identificador único do aluno (chave primária).
  - `nome_completo`: Nome completo do aluno.
  - `data_nascimento`: Data de nascimento do aluno.
  - `id_turma`: Identificador da turma do aluno (chave estrangeira).
  - `nome_responsavel`: Nome do responsável pelo aluno.
  - `telefone_responsavel`: Telefone do responsável.
  - `email_responsavel`: E-mail do responsável.
  - `informacoes_adicionais`: Informações adicionais sobre o aluno.

### 4. **Pagamento**
Registra os pagamentos realizados pelos alunos.
- **Colunas**:
  - `id_pagamento`: Identificador único do pagamento (chave primária).
  - `id_aluno`: Identificador do aluno (chave estrangeira).
  - `data_pagamento`: Data do pagamento.
  - `valor_pago`: Valor pago.
  - `forma_pagamento`: Forma de pagamento.
  - `referencia`: Referência do pagamento.
  - `status`: Status do pagamento.

### 5. **Presenca**
Registra a presença dos alunos.
- **Colunas**:
  - `id_presenca`: Identificador único da presença (chave primária).
  - `id_aluno`: Identificador do aluno (chave estrangeira).
  - `data_presenca`: Data da presença.
  - `presente`: Indica se o aluno estava presente (booleano).

### 6. **Atividade**
Armazena informações sobre atividades realizadas.
- **Colunas**:
  - `id_atividade`: Identificador único da atividade (chave primária).
  - `descricao`: Descrição da atividade.
  - `data_realizacao`: Data de realização da atividade.

### 7. **Atividade_Aluno**
Relaciona atividades com alunos.
- **Colunas**:
  - `id_atividade`: Identificador da atividade (chave estrangeira).
  - `id_aluno`: Identificador do aluno (chave estrangeira).

### 8. **Usuario**
Gerencia os usuários do sistema.
- **Colunas**:
  - `id_usuario`: Identificador único do usuário (chave primária).
  - `login`: Login do usuário.
  - `senha`: Senha do usuário.
  - `nivel_acesso`: Nível de acesso do usuário.
  - `id_professor`: Identificador do professor associado (chave estrangeira).

### 9. **Disciplina**
Lista as disciplinas disponíveis.
- **Colunas**:
  - `id_disciplina`: Identificador único da disciplina (chave primária).
  - `nome_disciplina`: Nome da disciplina.

### 10. **Nota**
Relaciona alunos, disciplinas e notas.
- **Colunas**:
  - `id_nota`: Identificador único da nota (chave primária).
  - `id_aluno`: Identificador do aluno (chave estrangeira).
  - `id_disciplina`: Identificador da disciplina (chave estrangeira).
  - `valor`: Valor da nota.

## Inserção de Dados

O script inclui exemplos de inserção de dados na tabela `Aluno`:

```sql
INSERT INTO Aluno (nome_completo, data_nascimento, id_turma, nome_responsavel, telefone_responsavel, email_responsavel, informacoes_adicionais) VALUES
('João Silva', '2005-01-15', NULL, 'Carlos Silva', '11999999999', 'carlos.silva@email.com', 'Nenhuma'),
('Maria Oliveira', '2006-03-22', NULL, 'Ana Oliveira', '21999999999', 'ana.oliveira@email.com', 'Nenhuma'),
('Pedro Santos', '2007-07-10', NULL, 'Roberto Santos', '71999999999', 'roberto.santos@email.com', 'Nenhuma');
```

## Configuração com Docker

Para facilitar a execução do projeto, você pode usar o Docker para configurar o banco de dados PostgreSQL.

### Pré-requisitos
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Passos para executar

1. **Crie um arquivo `docker-compose.yml` no diretório do projeto**:
   ```yaml
   version: '3.8'
   services:
     postgres:
       image: postgres:14
       container_name: projeto_escola_postgres
       environment:
         POSTGRES_USER: admin
         POSTGRES_PASSWORD: admin
         POSTGRES_DB: projeto_escola
       ports:
         - "5432:5432"
       volumes:
         - postgres_data:/var/lib/postgresql/data
       restart: always
   volumes:
     postgres_data:
   ```

2. **Inicie o container**:
   No terminal, execute:
   ```bash
   docker-compose up -d
   ```

3. **Acesse o banco de dados**:
   Use um cliente PostgreSQL (como `psql` ou ferramentas como DBeaver) para se conectar ao banco:
   - Host: `localhost`
   - Porta: `5432`
   - Usuário: `admin`
   - Senha: `admin`
   - Banco de dados: `projeto_escola`

4. **Execute o script SQL**:
   Carregue o arquivo `init.sql` no banco de dados:
   ```bash
   docker exec -i projeto_escola_postgres psql -U admin -d projeto_escola < postgres/init.sql
   ```

5. **Verifique os dados**:
   Após executar o script, as tabelas e os dados de exemplo estarão disponíveis no banco.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
=======
# Projeto Escola

Este projeto é um sistema de gerenciamento escolar desenvolvido em PostgreSQL. Ele contém a estrutura de tabelas e relacionamentos necessários para gerenciar professores, turmas, alunos, pagamentos, presenças, atividades, usuários, disciplinas e notas.

## Estrutura do Banco de Dados

O banco de dados é composto pelas seguintes tabelas:

### 1. **Professor**
Armazena informações sobre os professores.
- **Colunas**:
  - `id_professor`: Identificador único do professor (chave primária).
  - `nome_completo`: Nome completo do professor.
  - `email`: E-mail do professor.
  - `telefone`: Telefone do professor.

### 2. **Turma**
Relaciona turmas com professores.
- **Colunas**:
  - `id_turma`: Identificador único da turma (chave primária).
  - `nome_turma`: Nome da turma.
  - `id_professor`: Identificador do professor responsável (chave estrangeira).
  - `horario`: Horário da turma.

### 3. **Aluno**
Armazena informações sobre os alunos.
- **Colunas**:
  - `id_aluno`: Identificador único do aluno (chave primária).
  - `nome_completo`: Nome completo do aluno.
  - `data_nascimento`: Data de nascimento do aluno.
  - `id_turma`: Identificador da turma do aluno (chave estrangeira).
  - `nome_responsavel`: Nome do responsável pelo aluno.
  - `telefone_responsavel`: Telefone do responsável.
  - `email_responsavel`: E-mail do responsável.
  - `informacoes_adicionais`: Informações adicionais sobre o aluno.

### 4. **Pagamento**
Registra os pagamentos realizados pelos alunos.
- **Colunas**:
  - `id_pagamento`: Identificador único do pagamento (chave primária).
  - `id_aluno`: Identificador do aluno (chave estrangeira).
  - `data_pagamento`: Data do pagamento.
  - `valor_pago`: Valor pago.
  - `forma_pagamento`: Forma de pagamento.
  - `referencia`: Referência do pagamento.
  - `status`: Status do pagamento.

### 5. **Presenca**
Registra a presença dos alunos.
- **Colunas**:
  - `id_presenca`: Identificador único da presença (chave primária).
  - `id_aluno`: Identificador do aluno (chave estrangeira).
  - `data_presenca`: Data da presença.
  - `presente`: Indica se o aluno estava presente (booleano).

### 6. **Atividade**
Armazena informações sobre atividades realizadas.
- **Colunas**:
  - `id_atividade`: Identificador único da atividade (chave primária).
  - `descricao`: Descrição da atividade.
  - `data_realizacao`: Data de realização da atividade.

### 7. **Atividade_Aluno**
Relaciona atividades com alunos.
- **Colunas**:
  - `id_atividade`: Identificador da atividade (chave estrangeira).
  - `id_aluno`: Identificador do aluno (chave estrangeira).

### 8. **Usuario**
Gerencia os usuários do sistema.
- **Colunas**:
  - `id_usuario`: Identificador único do usuário (chave primária).
  - `login`: Login do usuário.
  - `senha`: Senha do usuário.
  - `nivel_acesso`: Nível de acesso do usuário.
  - `id_professor`: Identificador do professor associado (chave estrangeira).

### 9. **Disciplina**
Lista as disciplinas disponíveis.
- **Colunas**:
  - `id_disciplina`: Identificador único da disciplina (chave primária).
  - `nome_disciplina`: Nome da disciplina.

### 10. **Nota**
Relaciona alunos, disciplinas e notas.
- **Colunas**:
  - `id_nota`: Identificador único da nota (chave primária).
  - `id_aluno`: Identificador do aluno (chave estrangeira).
  - `id_disciplina`: Identificador da disciplina (chave estrangeira).
  - `valor`: Valor da nota.

## Inserção de Dados

O script inclui exemplos de inserção de dados na tabela `Aluno`:

```sql
INSERT INTO Aluno (nome_completo, data_nascimento, id_turma, nome_responsavel, telefone_responsavel, email_responsavel, informacoes_adicionais) VALUES
('João Silva', '2005-01-15', NULL, 'Carlos Silva', '11999999999', 'carlos.silva@email.com', 'Nenhuma'),
('Maria Oliveira', '2006-03-22', NULL, 'Ana Oliveira', '21999999999', 'ana.oliveira@email.com', 'Nenhuma'),
('Pedro Santos', '2007-07-10', NULL, 'Roberto Santos', '71999999999', 'roberto.santos@email.com', 'Nenhuma');
>>>>>>> 0f984844f2f1dc3fd506041216a356ac4bfbe7a8
