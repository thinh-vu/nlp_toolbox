from newspaper import Article

def web_to_text(url: str) -> str:
    """
    Downloads and parses the text of a webpage from a given URL.

    Args:
        url (str): The URL of the webpage to download.

    Returns:
        str: The text of the given page.
    """
    article = Article(url)
    article.download()
    article.parse()
    return article.text