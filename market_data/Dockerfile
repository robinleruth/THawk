FROM python:3.7-alpine

RUN apk add --no-cache gcc musl-dev make build-base libffi-dev openssl-dev postgresql-dev
RUN apk add build-base libtool automake

RUN adduser -D service

WORKDIR /home/service

COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/python -m pip install --upgrade pip
RUN venv/bin/pip install wheel
COPY dist dist
RUN venv/bin/pip install dist/*.whl
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY tests tests
COPY app.py run_app.sh ./

RUN chmod +x run_app.sh

RUN chown -R service:service ./
USER service
EXPOSE 8080

ENTRYPOINT ["./run_app.sh"]
