FROM python:3

WORKDIR /Event_Management

ADD . /Event_Management

RUN pip install -r requirements.txt

CMD [ "python", "wapp.py" ]