FROM python:3.8-alpine3.11

WORKDIR /worker

COPY requirments.txt .

RUN pip install -r ./requirments.txt

COPY worker/* ./

CMD python -u worker.py