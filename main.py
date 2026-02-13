from flask import Flask, render_template
from flask_socketio import SocketIO
#import stuff

app = Flask(__name__)
with open('venv/secret.txt', 'r') as f:
    key = f.read().strip()
app.config['SECRET_KEY'] = key
socketio = SocketIO(app)
#app stuff


@app.route('/')
def index():
    return render_template('index.html')
#the index page


if __name__ == '__main__':
    socketio.run(app)
