FROM python:3.10

COPY ./AppBlx /app/src
COPY requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "--host=0.0.0.0", "--reload"]
