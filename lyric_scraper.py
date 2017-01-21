from bs4 import BeautifulSoup
from collections import defaultdict
import os.path
import requests
import time
import Queue


lyrics_index_url = 'http://www.songlyrics.com/hip-hop-rap-lyrics.php'

response = requests.get(lyrics_index_url)

lyrics_index_content = response.content

lyrics_index = BeautifulSoup(lyrics_index_content, 'html.parser')

song_urls = Queue.Queue()
visited_urls = set()

def is_track_link(tag):
    if tag.name != 'a':
        return False

    if not tag.has_attr('href'):
        return False

    href = tag['href']

    if not href.endswith('-lyrics/'):
        return False

    if href.count('/') != 5:
        return False

    if href.endswith('/submit-lyrics/'):
        return False

    return True

def track_list_to_hrefs(track_list):
    return set([
        track['href'] for track in track_list
    ])

def add_song_url(url):
    if url in visited_urls:
        return

    song_urls.put(url)

    visited_urls.add(url)

def slugify(s):
    """
    Simplifies ugly strings into something URL-friendly.
    >>> print slugify("[Some] _ Article's Title--")
    some-articles-title

    Pulled from http://dolphm.com/slugify-a-string-in-python/
    """

    import re

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

def get_cache_file(url):
    from urlparse import urlparse

    parsed = urlparse(url)

    cache_name = slugify(parsed.path)

    return cache_name

track_list = lyrics_index.find_all(is_track_link)

for url in track_list_to_hrefs(track_list):
    add_song_url(url)

songs_by_genre = defaultdict(list)

while not song_urls.empty():
    url = song_urls.get()

    print('Current queue size: %d' % song_urls.qsize())

    cache_file = '_data/lyric_cache/%s.txt' % get_cache_file(url)

    if os.path.isfile(cache_file):
        continue

    time.sleep(0.1)

    print('Checking %s' % url)

    song_response = requests.get(url)
    song_content = song_response.content

    soup = BeautifulSoup(song_content, 'html.parser')

    lyrics = soup.find(id='songLyricsDiv')

    if lyrics is None:
        print('No lyrics found for %s' % url)
        continue

    lyrics = list(lyric.encode('ascii', 'ignore').strip() for lyric in lyrics.strings if lyric.strip())

    title_links = soup.select('.pagetitle p a')

    if len(title_links) < 3:
        print('Not enough parts found for %s' % url)
        continue

    artist, song, genre = title_links

    artist = artist.string.encode('ascii', 'ignore').strip()
    song = song.string.encode('ascii', 'ignore').strip()
    genre = genre.string.encode('ascii', 'ignore').strip()

    songs_by_genre[genre].append(
        (artist, song, lyrics)
    )

    with open(cache_file, 'w') as cache_handle:
        cache_handle.write(artist + '\n')
        cache_handle.write(song + '\n')
        cache_handle.write(genre + '\n\n')

        for lyric in lyrics:
            cache_handle.write(lyric + '\n')

    track_list = soup.find_all(is_track_link)

    for url in track_list_to_hrefs(track_list):
        add_song_url(url)

    print('Wrote cache %s' % cache_file)
