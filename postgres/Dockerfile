FROM postgres:14

COPY init.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_PASSWORD=faat
ENV POSTGRES_USER=faat
ENV POSTGRES_DB=escola

EXPOSE 5432
