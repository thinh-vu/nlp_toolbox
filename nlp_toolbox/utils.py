import shutil
import os
# import subprocess
import requests
from trafilatura import fetch_url, extract
import yaml

def lmt_detect():
    """Detect the running OS and return file path delimiter"""
    if os.name == 'nt':
        lmt = '\\'
    else:
        lmt = '/'
    return lmt

ROOT_DIR = os.path.abspath(os.curdir)
LMT = lmt_detect()

# DATA LOADING
## Read text file
def read_txt(path_to_file):
    """Read a plain text file"""
    with open(path_to_file) as f:
        content = f.read()
    return content

# API Request
def api_request(url, payload={}, method='GET'):
    """Request any API endpoints with a default User-Agent"""
    headers = {
        'accept-language': 'en-US,en;q=0.9',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-platform': '"macOS"',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
    response = requests.request(f"{method}", url, headers=headers, data=payload)
    return response.json()

## Convert Web to text
def web_to_text(url):
    downloaded = fetch_url(url)
    result = extract(downloaded)
    return result

# TRANSLATION
from deep_translator import GoogleTranslator
def translate(text, source='auto', target='en'):
    translate_text = GoogleTranslator(source=source, target=target).translate(text)
    return translate_text

# UTILITIES
## Memory cleaning
def memory_cleaner():
    """Free up memory from large model data"""
    import gc
    import torch
    gc.collect()
    torch.cuda.empty_cache()

## Get Google font
def get_google_font(font_family, delimiter=LMT):
    """Download & extract a Google font to local folder"""
    font_url = 'https://fonts.google.com/download?family={}'.format(font_family)
    response = requests.get(font_url)
    file_name = ROOT_DIR + delimiter + '{}.zip'.format(font_family)
    with open(file_name, 'wb') as f:
        f.write(response.content)
    shutil.unpack_archive(file_name, delimiter.join([ROOT_DIR, 'font', font_family]))