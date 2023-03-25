# Install pytesseract: https://tesseract-ocr.github.io/tessdoc/Installation.html

import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image

def image_to_text(image_path, language='vie'):
    text = pytesseract.image_to_string(Image.open(image_path), lang=language)
    return text