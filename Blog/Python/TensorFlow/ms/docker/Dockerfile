FROM python:3

RUN pip install tensorflow boto3 numpy

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./run.py" ]