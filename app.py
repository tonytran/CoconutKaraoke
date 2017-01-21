# Author: Michael Hawes, Gunther Cox, Kevin Brown, Tony Tran
# Coconut Karaoke
# 20 January 2017


from flask import Flask, render_template

app = Flask(__name__)

#app.config['MONGO_DBNAME'] = 'CK'  # CK = Coconut Karaoke
#app.config['MONGO_URI'] = 'mongodb://'   # add path for settings

#mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True) # start this webserver
