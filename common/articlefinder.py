import random
from pyquery import PyQuery


def get_article(article_request):
    pq = PyQuery(article_request.content)
    link_elements = pq('#main div div div ul li a')
    urls = [
        l.attrib["href"] for l in link_elements
    ]
    url = ""
    try:
        url = random.choice(urls)
    except IndexError:
        print("Search results page had not loaded article list")
    return url
