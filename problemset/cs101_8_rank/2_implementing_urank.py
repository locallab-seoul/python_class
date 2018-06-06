# Modify the crawl_web procedure so that instead of just returning the
# index, it returns an index and a graph. The graph should be a
# Dictionary where the key:value entries are:

#  url: [list of pages url links to]
from bs4 import BeautifulSoup
import pprint

def crawl_web(seed): # returns index, graph of outlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>:[list of pages it links to]
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)

            #Insert Code Here

            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


def get_page(url):
    try:
        import urllib.request
        return urllib.request.urlopen(url).read().decode("utf8")
    except:
        return None

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, html):
    bs = BeautifulSoup(html, 'html.parser')
    content = bs.get_text()
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None



index , graph = crawl_web('http://locallab-seoul.com/python/rank/index')

# pprint.pprint(graph)

# >>
# {'http://locallab-seoul.com/python/rank/arsenic': ['http://locallab-seoul.com/python/rank/nickel'],
#  'http://locallab-seoul.com/python/rank/hummus': [],
#  'http://locallab-seoul.com/python/rank/index': ['http://locallab-seoul.com/python/rank/hummus',
#                                                  'http://locallab-seoul.com/python/rank/arsenic',
#                                                  'http://locallab-seoul.com/python/rank/kathleen',
#                                                  'http://locallab-seoul.com/python/rank/nickel',
#                                                  'http://locallab-seoul.com/python/rank/zinc'],
#  'http://locallab-seoul.com/python/rank/kathleen': [],
#  'http://locallab-seoul.com/python/rank/nickel': ['http://locallab-seoul.com/python/rank/kathleen'],
#  'http://locallab-seoul.com/python/rank/zinc': ['http://locallab-seoul.com/python/rank/nickel',
#                                                 'http://locallab-seoul.com/python/rank/arsenic']}