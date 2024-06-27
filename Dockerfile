FROM python:3.9

ARG BATCH_SIZE=16
ARG EPOCHS=50

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y git libgl1-mesa-glx libglib2.0-0 && \
    apt-get clean

RUN git clone https://github.com/ultralytics/yolov5.git

WORKDIR /usr/src/app/yolov5

RUN pip install --no-cache-dir -r requirements.txt

COPY ../../Desktop/wtum_docker/dataset /usr/src/app/yolov5/dataset

ENV BATCH_SIZE ${BATCH_SIZE}
ENV EPOCHS ${EPOCHS}

ENTRYPOINT python train.py --img 640 --batch-size ${BATCH_SIZE} --epochs ${EPOCHS} --data dataset/data.yaml --weights yolov5s.pt