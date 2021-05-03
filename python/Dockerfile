# Dockerfile

FROM python:3.9.3-buster

WORKDIR /opencv-test

RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y

# Install dependencies
COPY requirements.txt .
COPY footage.mp4 .

RUN pip install -r requirements.txt

# Copy sourcecode
COPY main.py .

# Run
CMD ["python3", "main.py"]

