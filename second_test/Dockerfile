FROM python:3.8

ADD . ./second_test

WORKDIR ./second_test

RUN mkdir -p ./second_test/out

RUN pip install -r requirements.txt

ENV OUTPUT_DIRECTORY=./second_test/out

ENTRYPOINT ["python", "-m", "src.main"]