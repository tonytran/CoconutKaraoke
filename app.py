# Author: Michael Hawes, Gunther Cox, Kevin Brown, Tony Tran
# Coconut Karaoke
# 20 January 2017

import os
import jinja2
from flask import Flask, render_template, request, redirect, url_for, abort, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';

#app.config['MONGO_DBNAME'] = 'CK'  # CK = Coconut Karaoke
#app.config['MONGO_URI'] = 'mongodb://'   # add path for settings

#mongo = PyMongo(app)
note1 = "Crack mothers"
note2 = "crack babies and AIDS patients"
note3 = "Youngbloods can't spell"
note4 = "but they could rock you in PlayStation"

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == "POST":

            session['genre'] = request.form['genre']
            print(session['genre'])
            
            genre = session['genre']
            if genre.lower() == "edm":
                pass
                # retrieve lyrics from database and pass to lyrics()
                return redirect(url_for('lyrics'))

            elif genre.lower() == "classical":
                pass
                return redirect(url_for('lyrics'))

            elif genre.lower() == "pop":
                pass
                return redirect(url_for('lyrics'))

            else:
                raise ValueError('No lyrics matching your request were found')
                return redirect(url_for('index'))

            return redirect(url_for('lyrics'))
        return render_template('index.html')
    except:
        raise TypeError('could not process operation')




@app.route('/lyrics', methods=['GET', 'POST'])
def lyrics():
    listy = [note1,note2,note3,note4]
    if request.method == "POST":
        session['message'] = request.form['message1']  # get search text
        session['message'] += " " + request.form['message2']
        session['message'] += " " + request.form['message3']
        session['message'] += " " + request.form['message4']
        song_lyrics = session['message']
        print(song_lyrics)

        # if os.path.exists(path):
        #     filevar = open(path, 'a')
        # else:
        #     filevar = open(path, 'w')
        # filevar.write(str(session['message']))
        # filevar.write("\n")
        # filevar.close()
        return redirect(url_for('lyrics'))
    return render_template('lyrics.html', results=listy)


def retrieve_lyrics(genre,song_lyrics):
    path = './lyric_content/'+str(genre)+'.txt'
    if os.path.exists(path):
        filevar = open(path, 'a')
    else:
        filevar = open(path, 'w')
    filevar.write(str(song_lyrics))
    filevar.write("\n")
    filevar.close()


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
