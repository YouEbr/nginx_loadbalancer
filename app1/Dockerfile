FROM python:3

WORKDIR /

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY . /

CMD [ "python", "app.py" ]