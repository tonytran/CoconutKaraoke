# Author: Michael Hawes, Gunther Cox, Kevin Brown, Tony Tran
# Coconut Karaoke
# 20 January 2017

import os
from stack import Stack
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D'
S = Stack()


@app.route('/', methods=['GET', 'POST'])
def index():
    import urllib

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
        write_lyrics(song_lyrics)
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
    data = open_file(genre)
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
    return S.peek()


def write_lyrics(song_lyrics):
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
    filevar.close()


def open_file(genre):
    """
    opens and returns the last four lines in specified text file
    """
    path = 'lyric_content/'+str(genre)+'.txt'
    with open(path) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
    index = len(content)
    content = [content[index-4], content[index-3], content[index-2], content[index-1]]
    return content


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
