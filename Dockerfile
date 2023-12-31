# Use the official Python image as the base image
FROM python:3.11-slim
WORKDIR /code
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./myproject /code
RUN mkdir -p /code/sqlitedb
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
