import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template

sio = socketio.Server()
app = Flask(__name__)

@app.route('/')
def index():
    print('rendering template')
    return render_template('index.html')

@sio.on('connect', namespace='/motion')
def connect(sid, environ):
    print('connect ', sid)

@sio.on('motion event', namespace='/motion')
def message(sid, data):
    print('message ', data)
    sio.emit('reply', room=sid)

@sio.on('disconnect', namespace='/motion')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    app = socketio.Middleware(sio, app)

    eventlet.wsgi.server(eventlet.listen(('', 80)), app)