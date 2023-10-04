FROM python:3.11.6-alpine3.18

WORKDIR /usr/src/app

COPY requirements.txt  .

RUN pip install -r requirements.txt 

COPY src/ .

EXPOSE 8000

CMD ["python3", "-m","uvicorn", "main:app", "--host", "0.0.0.0"]