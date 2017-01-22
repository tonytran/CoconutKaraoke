
import os
import requests
import json
import re
import chardet

def get_tags():
    path = './caching/'

    files = os.listdir(path)
    taglist = []
    listofsongs = []
    for song_file in files:
        #print(song_file)
        jsondata = open(path+song_file).read()
        data = json.loads(jsondata)
        tags = []
        if 'track' in data:
            tags = data['track']['toptags']['tag']
            song = data['track']['name']
            artist = data['track']['artist']['name']
        if len(tags) != 0:

            for i in tags:
                taggedsong = (i, artist, song)
                taglist.append(taggedsong)




    return taglist


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

def main():


    tags = get_tags()
    #if len(tags) != 0:

    # print(result_list)
    #     #count += 1
    dictsets = {}
    pathtowrite = './caching2/'
    for t in tags: #tuple
        tag = t[0]['name']
        artist = t[1]
        song = t[2]
        genre_file = pathtowrite+tag+'.txt'
        song_item = artist + '-' + song
        if tag not in dictsets:
            dictsets[tag] = set()

            #genre = open(genre_file,'a')
            #genre.write(artist+'-'+ songinput)
            #genre.close()
        else:
            #print(type(song_item))
            item = song_item.encode('ascii','ignore')
            #print(item)
            dictsets[tag].add(item)
            #genre = open(genre_file, 'w')
            #genre.write(artist + '-' + songinput)
            #genre.close()
    #print(dictsets[tag])
    for tag in dictsets:
        #print(tag)
        try:
            file_to_write = (pathtowrite + tag + '.txt')
            # if type(file_to_write) == 'utf-8':
            #     file_to_write= file_to_write.decode('utf-8').encode('ascii')
            # else:
            file_to_write = file_to_write.encode('ascii','ignore')
            file_to_write = file_to_write.decode('ascii')
            #print(type(file_to_write))
            #encoding = chardet.detect(file_to_write)
            file_var = open(file_to_write, 'w')
            bigstring = ""
            for i in dictsets[tag]:
                #print(i)
                bigstring += i.decode('ascii') + '\n'


            file_var.write(bigstring)
            file_var.close()
        except Exception as e:
            print(e)
            
main()
