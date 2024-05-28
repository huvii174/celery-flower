FROM python:3.8

WORKDIR /app

COPY req.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0", "--port=5005"]
