FROM python:3.8

WORKDIR /src

COPY . /src/

RUN pip install -r /src/requirements.txt

RUN apt-get update

CMD [ "python3", "main.py" ]