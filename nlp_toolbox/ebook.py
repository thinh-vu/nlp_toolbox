## Read ebook files - ePub
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def read_epub_text(epub_path, filter=''):
    book = epub.read_epub(epub_path)
    chapters = book.get_items_of_type(ebooklib.ITEM_DOCUMENT)
    texts = {}
    if filter == '':
        for c in chapters:
            texts[c.get_name()] = chapter_to_str(c)
    else:
        for c in chapters:
            if filter in c.get_name():
                texts[c.get_name()] = chapter_to_str(c)
    return texts

def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.content, 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    return ' '.join(text)