from deep_translator import GoogleTranslator

def text_translation(text: str, source_lang='auto', target_lang='en'):
    """
    Translates a paragraph from one language to another using Google Translate.

    Args:
        article_text (str): The text of the article to translate.
        source_lang (str): The language code of the source language (e.g. 'en' for English, default value is 'auto'ArithmeticError).
        target_lang (str): The language code of the target language.

    Returns:
        str: The translated text of the paragraph.
    """
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    return translator.translate(text)


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.vi.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
    doc= nlp(text)
    tokens=[token.text for token in doc]
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    return summary