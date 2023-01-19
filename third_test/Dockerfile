FROM python:3.8

ADD . /third_test

WORKDIR /third_test

RUN mkdir -p /third_test/out

RUN pip install -r requirements.txt

ENV OUTPUT_FILE=/third_test/out/output.csv
ENV INPUT_FILE=/third_test/input/input.csv

ENTRYPOINT ["python", "-m", "src.main"]