FROM python:3.12

# Install SSH Client
RUN apt-get update && apt-get install -y openssh-client

# Set env variables
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Copy requirements.txt file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the aplication of the working directory
COPY . /app

# Start the SSH Tunnel
CMD python manage.py runserver 0.0.0.0:8000