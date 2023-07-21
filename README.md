# extracto


[Image Downloader Logo](https://example.com/image_downloader_logo.png)

extracto is a Python application that allows you to download images from a list of URLs. It uses asynchronous requests and is designed to be fast and memory-efficient. You can run the application either directly on your local computer or using Docker for easy setup and isolation.

## Features

- Download images from a list of URLs provided in a text file.
- Check for valid image URLs using regular expressions.
- Download images concurrently to save time.
- Handle errors gracefully and report failed downloads.

## Requirements

- Python 3.8 or later
- Docker (optional, for running with Docker)

## Getting Started

### Running Locally

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/koiic/extracto.git
   cd extracto
   create a virtual environment and activate it
   example: python3 -m venv venv or virtualenv venv
    source venv/bin/activate . (linux)
    venv\Scripts\activate (windows)
   pip install -r requirements.txt
    ```
   
2. You can use the already added txt file or create a text file containing the URLs of the images you want to download. Each URL should be on a separate line. For example:

   ```text
    https://example.com/image1.jpg
    https://example.com/image2.jpg
    https://example.com/image3.jpg
    ```
   - If you want to use the already added txt file, you can skip this step.
   
3. Run the application:

   ```bash
    python app.py --filepath <path-to-input-file> --output_dir <path-to-output_directory>
    ```

    For example: using the already added txt file

    ```bash
    python app.py --filepath test_images_url.txt --output_dir <path-to-output_directory>
    ```
   you will see the logs in the terminal and the images will be downloaded to the specified output directory. If the directory does not exist, it will be created automatically. If the directory does not exist, it will be created automatically.
4. (Optional) Run the tests:

   ```bash
   pytest
   ```
   
### Running with Docker

1. Clone the repository to your local machine:

   ```bash
    git clone https://github.com/koiic/extracto.git
    cd extracto
    ```
   
2 Build the Docker image:

   ```bash
   docker build -t extracto .
   ```

1. Create a text file containing the URLs of the images you want to download. Each URL should be on a separate line. For example:

   ```text
    https://example.com/image1.jpg
    https://example.com/image2.jpg
    https://example.com/image3.jpg
    ```
   
2. Run the application:

   ```bash
   docker run -v <path-to-input-file>:/app/test_image_urls.txt -v <path-to-output_directory>:/app/images image-downloader
   ```
   
   For example:

   ```bash
   docker run -v </path/to/txt/file>:/app/test_image_urls.txt -v </path/to/download/folder>:/app/images extracto --filepath /app/test_images_url.txt --output_dir /app/output

   ```
   
   The images will be downloaded to the specified output directory. If the directory does not exist, it will be created automatically.
