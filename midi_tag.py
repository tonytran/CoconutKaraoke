
#import FileNotFoundException

import time
def get_tracklist(path, **kwargs ):

    listy = []
    try:
        listy = os.listdir(path)
        #list2  = lambda x: x.replace('.mid', ''), listy
    except Exception as e:
        pass

    return listy

def get_artist(path):

    #artists = list_artists(path)
    charlist = []
    artist = path.split('\\')[4]
    #print(artist)
    for char in artist:
        charlist.append(char)
    if '_' in charlist:
        artist = artist.replace('_', ' ')

    return artist
def list_artists(path):
    return os.listdir(path)
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

def get_tags(base, artist, song, apikey):
    test = []
    slugifiedname = path+slugify(artist) +'-'+slugify(song[:25])
    path = './_data/caching/'+slugifiedname+'.json'

    if not os.path.exists(path):

    #for li in track_list:
        song = (song.replace('.mid', ''))

        url = (base.replace('{k}', apikey))
        url = (url.replace('{a}', artist.lstrip()))
        url = (url.replace('{t}', song))
        #print(url)
        time.sleep(.1)
        r = requests.get(url)

        #print(r.status_code)

        if r.status_code == 200:
            if not os.path.exists(path):
                jsonfile = open(path,'w')
                json.dump(r.json(), jsonfile)
                jsonfile.close()
        jsondata = r.json()
    else:
        jsondata = open(path).read()
    tags = []
    if 'track' in jsondata:
        tags = jsondata['track']['toptags']
        for i in tags:
            tags.append(i['name'])
    return tags


#    test =  json['track']['toptags']['tag']

def write_to_file():
    pass


def main():
    apikey = open('api_key.txt').readline().strip('\n')
    
    path = "D:\Downloads\clean_midi\clean_midi"

    base = "http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={k}&artist={a}&track={t}&format=json"
    artists = list_artists(path)
    count = 0
    pathtowrite =  './_data/midifiles/'
    dictsets={}
    for i in artists:
    #    print(i)
        #artist = get_artist(path+'\\' + i)

        artist = get_artist(path+'\\'+i)
        #print(path)

        listy = get_tracklist(path+'\\'+i)
        for songinput in listy:
            tags = get_tags(base, artist, songinput, apikey)



main()
