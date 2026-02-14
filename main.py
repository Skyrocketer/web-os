from flask import Flask, render_template
from flask_socketio import SocketIO
import os
#import stuff

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
socketio = SocketIO(app)
#app stuff


@app.route('/')
def index():
    return render_template('index.html')
#the index page

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404
#handle requests with no index

if __name__ == '__main__':
    socketio.run(app)
