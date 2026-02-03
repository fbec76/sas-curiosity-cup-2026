FROM postgres:15
COPY seeds /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/restore.sh