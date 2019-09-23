import os
import flask, flask_socketio, flask_sqlalchemy

import models

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

@app.route('/')

def index():
    messages = models.Message.query.all()
    chat = [m.text for m in messages]
    print(chat)
    return flask.render_template("index.html")

@socketio.on('connect')
def on_connect():
    print('someone connected')
    
    flask_socketio.emit('update', {
        'data': 'Got your connection!'
    })
@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')
    
    flask_socketio.emit('update', {
        'data': 'Disconnected'
    })

@socketio.on('new number')
def on_new_number(data):
    print(("Got an event for new number with data:"), data)
    rand_number = data['number']
    
    socketio.emit('number received', {
        'number': rand_number
    })
    
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )