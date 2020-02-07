FROM python:3.8-alpine3.11

WORKDIR /distributer

COPY requirments.txt .

RUN pip install -r ./requirments.txt

COPY distributer/* ./

CMD python -u distributer.py