FROM python:3.10.0-slim
WORKDIR /code
EXPOSE 8000
COPY ../fastApiProject/python-db-test/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ../fastApiProject/python-db-test/myproject /code
RUN mkdir -p /code/sqlitedb
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]