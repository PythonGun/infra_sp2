FROM python:3.7-slim
RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir
RUN pip install psycopg2-binary==2.9

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
