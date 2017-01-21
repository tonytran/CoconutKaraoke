# Author: Michael Hawes, Gunther Cox, Kevin Brown, Tony Tran
# Coconut Karaoke
# 20 January 2017

import urllib
from stack import Stack

import os
from stack import Stack
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D'
S = Stack()


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
            push_genre(genre)  # throw genre in stack to allow us to grab later
            listy = open_file(genre)   # retrieve lyrics from text file
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
        session['message'] = request.form['message1']
        session['message'] += " " + request.form['message2']
        session['message'] += " " + request.form['message3']
        session['message'] += " " + request.form['message4']
        song_lyrics = session['message']
        genre = get_genre()
        write_lyrics(genre, song_lyrics)
        return redirect(url_for('music'))

    if 'listy' in request.args:
        listy_string = request.args.get('listy')
        listy = listy_string.split('@')
    else:
        listy = []

    return render_template('lyrics.html', results=listy)


@app.route('/music')
def music():
    genre = get_genre()
    data = return_lyrics(genre)
    return render_template('music.html', results=data)




#==============Generic Functions===============================================
def push_genre(genre):
    """
    pushes most recently selected genre to stack
    """
    S.push(genre)

def get_genre():
    """
    returns most recent genre chosen
    """
    if S.isEmpty():
        return 'no-genre'
    else:
        return S.peek()


def write_lyrics(genre, song_lyrics):
    """
    writes users lyrics to a specified text file
    """
    genre = get_genre()
    path = 'lyric_content/'+str(genre)+'.txt'
    if os.path.exists(path):
        filevar = open(path, 'a')
    else:
        filevar = open(path, 'w')
    filevar.write(str(song_lyrics))
    filevar.write('\n')
    path = os.path.join('lyric_content', genre + '.txt')
    filevar = open(path, 'a+')
    filevar.write(str(song_lyrics) + os.linesep)
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
    index = len(content)
    content = [content[-4], content[-3], content[-2], content[-1]]
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
