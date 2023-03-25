# I. GENERATE WORDS CLOUD
from wordcloud import WordCloud
from ur_gadget import get_google_font

# Words tokenize
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from collections import Counter

# Visualization with Matplotlib
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

def wordcloud_gen (text, font_path=None, limit=100, color_map='magma', bg_color='white', font_size=300, fig_size= (20,20), width=1024, height=800, interpolation='bilinear'):
    if font_path is None:
        custom_font = None
    else:
        custom_font = font_path

    wordcloud = WordCloud(background_color=bg_color, 
                        max_words=limit,
                        max_font_size=font_size,
                        width=width, 
                        height=height,
                        colormap=color_map,
                        font_path = custom_font
                        ).generate(text)

    plt.figure(figsize=fig_size)
    plt.imshow(wordcloud, interpolation=interpolation)
    plt.axis("off")
    plt.margins(x=0, y=0)
    return plt.show()

def word_tokenize_stats(text):
    c = Counter(word_tokenize(text))
    df = pd.DataFrame.from_records(list(dict(c).items()), columns=['word','count']).sort_values(by='count', ascending=False).reset_index(drop=True)
    return df