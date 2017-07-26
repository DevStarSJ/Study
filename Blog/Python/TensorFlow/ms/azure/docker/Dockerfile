FROM python:3

RUN pip install tensorflow azure numpy

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./run.py" ]