# Use the official Python image as the base image
FROM python:3.10.0-slim

# Set the working directory to /code
WORKDIR /code

# Copy the requirements file to the working directory
COPY fastApiProject2/requirements.txt /code/requirements.txt

# Install the required dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of the application code to the working directory
COPY fastApiProject2 /code

# Create a directory for SQLite database
RUN mkdir -p /code/sqlitedb

# Specify the default command to run when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
