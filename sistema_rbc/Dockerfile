FROM python:3.9


WORKDIR /usr/app/src

COPY . .

RUN apt-get update && apt-get install -y libgl1-mesa-glx libxkbcommon-x11-0

RUN pip install -r requirements.txt