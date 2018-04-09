import matplotlib.pyplot as plt

def get_page(url):
    try:
        import urllib.request
        return urllib.request.urlopen(url).read().decode("utf-8")
    except:
        return ""


def hash_string(keyword, buckets):
    pass


def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []

    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] += 1
            keys_used.append(w)

    return results


words = get_page('http://www.gutenberg.org/cache/epub/1661/pg1661.txt').split()
counts = test_hash_function(hash_string, words, 12)
print(counts)
counts = test_hash_function(hash_string, words, 100)
print(counts)

plt.bar(range(len(counts)), counts)
plt.show()
