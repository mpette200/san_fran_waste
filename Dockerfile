
FROM python:3.7.8-buster AS base
WORKDIR /garbage
COPY requirements.txt .
RUN pip install -r requirements.txt

# uWSGI -- latest LTS (long term support) release,
RUN pip install https://projects.unbit.it/downloads/uwsgi-lts.tar.gz
# RUN pip install uwsgi

COPY src/*.py src/
COPY src/assets src/assets

# uwsgi --http 127.0.0.1:xxxx --module myproject:app
# uwsgi --http 0.0.0.0:80 --wsgi-file webapp.py --callable server
WORKDIR /garbage/src
EXPOSE 80
CMD uwsgi --http 0.0.0.0:$PORT --wsgi-file webapp.py --callable server
