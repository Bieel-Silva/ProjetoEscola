import os
import time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://faat:faat@postgres:5432/escola"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db_connection():
    """Estabelece conexão com o banco de dados PostgreSQL."""
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts:
        try:
            conn = psycopg2.connect(
                host=os.environ.get('DATABASE_HOST', 'postgres'),
                database=os.environ.get('DATABASE_NAME', 'app_database'),
                user=os.environ.get('DATABASE_USER', 'postgres'),
                password=os.environ.get('DATABASE_PASSWORD', 'postgres')
            )
            print("Conexão com o banco de dados estabelecida com sucesso!")
            return conn
        except psycopg2.OperationalError:
            attempts += 1
            print(
                f"Tentativa {attempts} de conexão com o banco de dados falhou. "
                "Tentando novamente em 5 segundos..."
            )
            time.sleep(5)

    raise Exception("Não foi possível conectar ao banco de dados após várias tentativas.")

def close_db_connection(conn):
    """Fecha a conexão com o banco de dados."""
    if conn:
        conn.close()
        print("Conexão com o banco de dados foi fechada.")