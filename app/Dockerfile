FROM tiangolo/uwsgi-nginx-flask:flask-python3.5

RUN apt update

COPY . /app

RUN pip3 install -r /app/requirements.txt