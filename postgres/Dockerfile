FROM postgres:14

COPY init.sql /docker-entrypoint-initdb.d/
# Define argumentos e variáveis de ambiente
ENV POSTGRES_PASSWORD=faat
ENV POSTGRES_USER=faat
ENV POSTGRES_DB=escola
# Expõe a porta padrão do PostgreSQL
EXPOSE 5432
