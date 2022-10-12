FROM ubuntu:20.04

WORKDIR /app

RUN apt update
RUN apt upgrade -y

RUN apt install ffmpeg libsm6 libxext6  -y

COPY requirements.txt ./
COPY gesture_recognition ./gesture_recognition/
COPY main.py ./

RUN apt -y install python3-pip

RUN pip3 install -r requirements.txt

EXPOSE 8765

CMD ["python3", "./main.py"]
