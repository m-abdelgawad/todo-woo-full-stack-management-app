FROM postgres:14.8

# Environment variables
ENV POSTGRES_USER=databaseuser
ENV POSTGRES_PASSWORD=B6vXq5Wm8*0k4234
ENV POSTGRES_DB=todowoo

# Copy initialization script
COPY init.sql /docker-entrypoint-initdb.d/
