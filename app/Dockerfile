FROM python:3.10

RUN apt-get update

RUN apt-get install -y netcat-openbsd apt-utils

RUN pip install --upgrade pip

WORKDIR /website

# Copy only the requirements file first
COPY req.txt .

# Install dependencies from the requirements file
RUN pip install -r req.txt

# Copy the rest of the application code
COPY . .

# Collect static
RUN python manage.py collectstatic --noinput

ENV PYTHONUNBUFFERED=1

# Run the app using customised bash script
ENTRYPOINT ["bash", "entrypoint.sh"]
