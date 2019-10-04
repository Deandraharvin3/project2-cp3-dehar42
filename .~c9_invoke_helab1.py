import os
import flask, flask_socketio,psycopg2
import models, chatbot
from rfc3987 import parse

app = flask.Flask(__name__)


socketio = flask_socketio.SocketIO(app)
 
@app.route('/')

def index():
    return flask.render_template("index.html")

@socketio.on('connect')
def on_connect():
    print('someone connected')
    messages = models.Message.query.all()
    chat = [m.text + '\n' for m in messages]
    flask_socketio.emit('update', {
        'data': 'Got your connection!',
        'previous_messages': chat
    })

@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')
    
    flask_socketio.emit('update', {
        'data': 'Disconnected'
    })

def query(url):
    messages = models.Message.query.all()
    chat = [m.text + '\n' for m in messages]

    socketio.emit('message received', {
        'message': chat,
        'isURL': url
    })
   
    
@socketio.on('new message')
def on_new_number(data):
    url = False
    print(("Got an event for new number with data:"), data)
    new_message = models.Message(data['message'])
    models.db.session.add(new_message)
    models.db.session.commit()
    if new_message[:4] == 'http':
        parse(new_message, rule='IRI')
        url = True
    if new_message[:2] == '!!':
        chatbot.Chatbot.get_response(new_message[2:len(new_message)])
    query(url)
    
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )