# Change the lookup procedure
# to now work with dictionaries.


def get_page(url):
    try:
        import urllib.request
        return urllib.request.urlopen(url).read().decode("utf8")
    except:
        return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:   # not found, add new keyword to index 
        index[keyword] = [url]


def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index


def lookup(index, keyword):
    pass


# table = crawl_web('http://locallab-seoul.com/python/rank/index')
# result = lookup(table,'<html>')
# print(result)
