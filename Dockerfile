FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends libgomp1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app
COPY downloader.py /app
COPY test_image_downloader.py /app
COPY test_images_url.txt /app

ENTRYPOINT ["python", "app.py"]
