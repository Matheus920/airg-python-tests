FROM python:3.8

ADD . ./first_test

WORKDIR ./first_test

RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]