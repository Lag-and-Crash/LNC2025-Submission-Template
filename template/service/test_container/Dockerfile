FROM python:3.7.13-alpine3.16

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]

EXPOSE 1337