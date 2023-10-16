# Use the official Python image from Docker Hub
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container using pipenv file and lock file

COPY Pipfile Pipfile.lock /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir pipenv && pipenv install --system

# Copy the rest of the application code into the container
COPY . /app/

# Expose a port if your application needs it
# EXPOSE 8000

# Make the gunicorn_start.sh script executable
RUN chmod +x entrypoint.sh

# Define the command to run your application
CMD ["./entrypoint.sh"]
