import os
import re
listof = os.listdir('./caching')

newlistof = []
def slugify(s):
    """
    Simplifies ugly strings into something URL-friendly.
    >>> print slugify("[Some] _ Article's Title--")
    some-articles-title
    """

    # "[Some] _ Article's Title--"
    # "[some] _ article's title--"
    s = s.lower()

    # "[some] _ article's_title--"
    # "[some]___article's_title__"
    for c in [' ', '-', '.', '/']:
        s = s.replace(c, '_')

    # "[some]___article's_title__"
    # "some___articles_title__"
    s = re.sub('\W', '', s)

    # "some___articles_title__"
    # "some   articles title  "
    s = s.replace('_', ' ')

    # "some   articles title  "
    # "some articles title "
    s = re.sub('\s+', ' ', s)

    # "some articles title "
    # "some articles title"
    s = s.strip()

    # "some articles title"
    # "some-articles-title"
    s = s.replace(' ', '-')

    return s
for filename in listof:
    filename = filename.rstrip('.json')
    newname = slugify(filename)
    newlistof.append(newname)


for i in range(len(listof)):
    if not os.path.exists('./caching/'+str(newlistof[i])+'.json'):
        os.rename('./caching/'+str(listof[i]), './caching/'+str(newlistof[i]+'.json'))
