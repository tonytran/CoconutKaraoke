# Author: Michael Hawes, Gunther Cox, Kevin Brown, Tony Tran
# Coconut Karaoke
# 20 January 2017

import urllib
import random
import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D'


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":

        # The valid genre types
        genres = [
            'edm',
            'classical',
            'pop'
        ]

        genre = request.form['genre']    # retrieve genre from user

        genre = genre.lower()

        if genre in genres:
            # Add the genre to stack to allow us to get later
            session['genre'] = genre
            listy = open_file(genre)   # retrieve lyrics from text file
            listy = [listy[-4], listy[-3], listy[-2], listy[-1]]
            listy_string = urllib.parse.quote("@".join(listy))

            # Pass lyrics to the next page by adding them as a url parameter
            return redirect(url_for('lyrics')+'?listy='+listy_string)
        else:
            raise ValueError('No lyrics matching your request were found')
            return redirect(url_for('index'))

    return render_template('index.html')





@app.route('/lyrics', methods=['GET', 'POST'])
def lyrics():

    if request.method == "POST":

        # Retrieve the input that was entered in the form
        line1 = request.form['message1']
        line2 = request.form['message2']
        line3 = request.form['message3']
        line4 = request.form['message4']

        genre = session.get('genre', 'no-genre')
        write_lyrics(genre, line1, line2, line3, line4)
        return redirect(url_for('music'))

    if 'listy' in request.args:
        listy_string = request.args.get('listy')
        listy = listy_string.split('@')
    else:
        listy = []

    return render_template('lyrics.html', results=listy)


@app.route('/music')
def music():
    genre = session.get('genre', 'no-genre')
    data = return_lyrics(genre)
    name = rand_song_title()
    print(name)
    if request.method == "POST":
        play = request.form['play']
        pause = request.form['pause']
        if play == True:
            pass
            #play song here
        elif pause == True:
            pass
            #pause song here
        else:
            raise TypeError('Please press play or pause')
    return render_template('music.html', results=data, title=name)




#==============Generic Functions===============================================
def play_music():
    """
    plays an audio file (.wav, .ogg)
    """
    import pyglet
    song = pyglet.media.load('audio file goes here')
    song.play()
    pyglet.app.run()


def rand_song_title():
    """
    returns a random song title
    """
    genre = str('names')
    titles = open_file(genre)
    num = random.randint(0, len(titles)-1)
    song_title = titles[num]
    return song_title


def write_lyrics(genre, line1, line2, line3, line4):
    """
    writes users lyrics to a specified text file
    """
    path = 'lyric_content/'+str(genre)+'.txt'
    if os.path.exists(path):
        filevar = open(path, 'a')
    else:
        filevar = open(path, 'w')
    filevar.write(str(line1))
    filevar.write('\n')
    filevar.write(str(line2))
    filevar.write('\n')
    filevar.write(str(line3))
    filevar.write('\n')
    filevar.write(str(line4))
    filevar.write('\n')
    path = os.path.join('lyric_content', genre + '.txt')
    filevar = open(path, 'a+')
    filevar.close()


def open_file(genre):
    """
    opens and returns the last four lines in specified text file
    """
    path = os.path.join('lyric_content', genre + '.txt')
    with open(path) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
    return content


def return_lyrics(genre):
    """
    opens and returns the lyrics in specified text file
    """
    path = 'lyric_content/'+str(genre)+'.txt'
    with open(path) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
    return content


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
