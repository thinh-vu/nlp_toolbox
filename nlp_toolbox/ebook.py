## Read ebook files - ePub
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def read_epub_text(epub_path, filter=''):
    chapters = get_chapter(epub_path)
    texts = {}
    if filter == '':
        for c in chapters:
            texts[c.get_name()] = chapter_to_str(c)
    else:
        for c in chapters:
            if filter in c.get_name():
                texts[c.get_name()] = chapter_to_str(c)
    return texts

def get_chapter(epub_path):
    book = epub.read_epub(epub_path)
    chapters = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
    return [c.get_name() for c in chapters]

def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    return ' '.join(text)