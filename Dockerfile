FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get install -y python3-pyqt5 qttools5-dev-tools build-base linux-headers && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
