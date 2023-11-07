FROM python:3.11

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app /app/

CMD [ "python3", "/app/main.py"]
