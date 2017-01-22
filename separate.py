#rock and pop
import os


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

    oldpath = "C:\\Users\\tonyb\\pennappsfall\\CoconutKaraoke\\midifiles\\clean_midi"
    newpath = "C:\\Users\\tonyb\\pennappsfall\\CoconutKaraoke\\midifiles\\clean_midi\\genres"
    path = '.\_data\caching2\\'
    rockfiles = open(path+'rock.txt', 'r')
    #popfiles = open(path+'pop.txt', 'r')

    try:
        # for line in rockfiles:
        #     info = line.split('-')
        #     artist = info[0]
        #     track = info[1].strip('\n')
        #     #print(artist, track)
        #     if os.path.isfile(oldpath+'\\'+artist+'\\'+track+'.mid'):
        #         if not os.path.exists(oldpath+'\\'+artist+'\\'+track+'.mid'):
        #             if not os.path.exists(newpath+'\\'+'rock\\'+track+'.mid'):
        #                 os.rename(oldpath+'\\'+artist+'\\'+track+'.mid', newpath+'\\'+'rock\\'+track+'.mid')
        for line in rockfiles:
            info = line.split('-')
            artist = info[0]
            track = info[1].strip('\n')
            #print(artist, track)
            if os.path.isfile(oldpath+'\\'+artist+'\\'+track+'.mid'):
                print(1)
                if not os.path.exists(newpath+'\\'+'rock\\'+track+'.mid'):
                    os.rename(oldpath+'\\'+artist+'\\'+track+'.mid', newpath+'\\'+'rock\\'+track+'.mid')
                    print('success')
    except Exception as e:
        print(e)
    except WindowsError as e:
        print(e)

main()
