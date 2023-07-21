"""
Functions implementation for downloading image from a list of urls in a text file.
"""
import os
from typing import Match

import aiofiles
import asyncio
import re
from urllib.parse import urlsplit

import aiohttp


async def is_valid_image_url(url: str):
    # Regular expression to match common image file extensions
    image_extensions = r"\.(jpg|jpeg|png|gif|bmp)$"
    return re.search(image_extensions, url, re.IGNORECASE) is not None


async def download_image(session, url, output_dir):
    """
    Download image from a given url and save it to the output directory
    :param session: requests session
    :param url:  image url
    :param output_dir:  output directory
    :return:  None
    """
    try:
        async with session.get(url) as response:
            if response.status == 200:
                filename = os.path.join(output_dir, os.path.basename(urlsplit(url).path))
                async with aiofiles.open(filename, 'wb') as f:
                    while True:
                        chunk = await response.content.read(8192)
                        if not chunk:
                            break
                        await f.write(chunk)
            else:
                print(f"Failed to download {url}. Status code: {response.status}")
    except Exception as e:
        print(f"Error while downloading {url}: {e}")


async def download_images_from_file(file_path, output_dir, batch_size=100):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    async with aiohttp.ClientSession() as session:
        with open(file_path, 'r') as f:
            urls = f.read().split()

        tasks = [download_image(session, url, output_dir) for url in urls if await is_valid_image_url(url)]
        await asyncio.gather(*tasks)
