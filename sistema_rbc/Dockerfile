FROM python:3.9


WORKDIR /usr/app/src

COPY . .

RUN apt-get update && apt-get install -y libgl1-mesa-glx

RUN pip install -r requirements.txt