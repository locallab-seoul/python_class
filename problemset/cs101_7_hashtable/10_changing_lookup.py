# Change the lookup procedure
# to now work with dictionaries.


def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None

# table = {'udacity': ['http://udacity.com', 'http://npr.org']}
# print(lookup(table, 'computing'))
# >>> None

# table = {'udacity' : ['http://udacity.com', 'http://npr.org'],
#          'computing': ['http://acm.org']}
# print(lookup(table, 'computing'))
# >>> ['http://acm.org']
