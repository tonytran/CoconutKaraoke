# Author: Michael Hawes, Gunther Cox, Kevin Brown, Tony Tran
# Coconut Karaoke
# 20 January 2017

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

    listy = [note1,note2,note3,note4]
    if request.method == "POST":
        session['message'] = request.form['message']  # get search text
        print(session['message'])
        return redirect(url_for('index'))
    return render_template('index.html', results=listy)


if __name__ == '__main__':
    app.run(debug=True) # start this webserver
