#Dockerfile, Image,Container
FROM python:3.9
WORKDIR /interview
COPY ./requirements.txt .
RUN pip install Flask
RUN pip install -r requirements.txt

COPY src/ .

CMD ["python", "./server.py"]