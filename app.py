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

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":

        session['genre'] = request.form['genre']    # retrieve genre from user
        genre = session['genre']
        genre = genre.lower()

        if genre == "edm" or genre == "classical" or genre == "pop":
            listy = open_file(genre)   # retrieve lyrics from text file
            listy_string = "@".join(listy).replace(" ", "+")
            print(listy_string)
            #lyrics(listy)
            return redirect(url_for('lyrics')+'?listy='+listy_string)

        else:
            raise ValueError('No lyrics matching your request were found')
            return redirect(url_for('index'))

        return redirect(url_for('lyrics'))
    return render_template('index.html')





@app.route('/lyrics', methods=['GET', 'POST'])
def lyrics():
    listy_string = request.args.get('listy')
    listy = listy_string.split('@')
    #listy = ["hii", "hello"]
    if request.method == "POST":
        session['message'] = request.form['message1']            # get input texts
        session['message'] += " " + request.form['message2']
        session['message'] += " " + request.form['message3']
        session['message'] += " " + request.form['message4']
        song_lyrics = session['message']

        return redirect(url_for('lyrics'))
    return render_template('lyrics.html', results=listy)


def write_lyrics(genre, song_lyrics):
    """
    writes users lyrics to a specified text file
    """
    path = './lyric_content/'+str(genre)+'.txt'
    if os.path.exists(path):
        filevar = open(path, 'a')
    else:
        filevar = open(path, 'w')
    filevar.write(str(song_lyrics))
    filevar.write("\n")
    filevar.close()


<<<<<<< HEAD
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




=======
>>>>>>> 7b5236ae48871d67ccc6ab833c28fa59d22026b5
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
