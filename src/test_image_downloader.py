import os
from urllib.parse import urlsplit

import pytest
import aiohttp
import asyncio
from downloader import is_valid_image_url, download_image, download_images_from_file


# Test if the is_valid_image_url function correctly identifies valid image URLs
def test_is_valid_image_url_valid_urls():
    valid_urls = [
        "https://example.com/image1.jpg",
        "https://example.com/image2.png",
        "https://example.com/image3.gif",
    ]

    for url in valid_urls:
        assert asyncio.run(is_valid_image_url(url)) is True


# Test if the is_valid_image_url function correctly identifies invalid URLs
def test_is_valid_image_url_invalid_urls():
    invalid_urls = [
        "https://example.com/document1.pdf",
        "https://example.com/image1.mp4",
        "https://example.com/data.xlsx",
    ]

    for url in invalid_urls:
        assert asyncio.run(is_valid_image_url(url)) is False


# Test if the download_image function correctly downloads a valid image
@pytest.mark.asyncio
async def test_download_image_valid_image(tmpdir):
    output_dir = tmpdir.mkdir("output")

    valid_image_url = "https://via.placeholder.com/150"

    async with aiohttp.ClientSession() as session:
        await download_image(session, valid_image_url, output_dir)

    filename = os.path.basename(urlsplit(valid_image_url).path)
    assert os.path.exists(os.path.join(output_dir, filename))


# Test if the download_image function handles invalid URLs gracefully
@pytest.mark.asyncio
async def test_download_image_invalid_url(tmpdir):
    output_dir = tmpdir.mkdir("output")

    invalid_image_url = "https://example.com/non_existent_image.jpg"

    async with aiohttp.ClientSession() as session:
        await download_image(session, invalid_image_url, output_dir)

    filename = os.path.basename(urlsplit(invalid_image_url).path)
    assert not os.path.exists(os.path.join(output_dir, filename))


# Test if the download_images_from_file function correctly downloads images from a file
@pytest.mark.asyncio
async def test_download_images_from_file(tmpdir):
    output_dir = tmpdir.mkdir("output")
    file_path = os.path.join(tmpdir, "test_urls.txt")

    with open(file_path, "w") as f:
        f.write(
            "https://via.placeholder.com/150\n"
            "https://via.placeholder.com/250\n"
            "https://via.placeholder.com/350\n"
            "http://i0.kym-cdn.com/entries/icons/original/000/002/232/bullet_cat.jpg\n"
        )

    await download_images_from_file(file_path, output_dir)

    print(os.listdir(output_dir))

    assert len(os.listdir(output_dir)) == 1


# Add more test cases for edge cases, handling empty files, non-existent files, etc.
# Use the tmpdir fixture to delete all created files and directories after each test
@pytest.fixture(autouse=True)
def cleanup(tmpdir):
    yield
    tmpdir.remove(ignore_errors=True)
