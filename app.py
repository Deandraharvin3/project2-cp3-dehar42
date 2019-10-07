import os
import flask, flask_socketio,psycopg2
import models, chatbot
from urlparse import urlparse

app = flask.Flask(__name__)


socketio = flask_socketio.SocketIO(app)
 
@app.route('/')

def index():
    messages = models.Message.query.all()
    chat = [m.text + "\n" for m in messages]
    return flask.render_template( "index.html")

@socketio.on('connect')
def on_connect():
    print('someone connected')
    messages = models.Message.query.all()
    chat = [m.text + "\n" for m in messages]
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

def query(isurl, new_message):
    messages = models.Message.query.all()
    chat = [m.text + '\n' for m in messages]
    socketio.emit('message received', {
        'chat': chat[0:len(chat)-1],
        'message': new_message,
        'url': isurl
    })
   
    
@socketio.on('new message')
def on_new_number(data):
    url = False
    print(("Got an event for new number with data:"), data)
    new_message = models.Message(data['message'])
    models.db.session.add(new_message)
    models.db.session.commit()
    
    #checking if the messahe is a link
    if urlparse(data['message']).scheme != '':
        print('Received a URL')
        url = True
        
    if data['message'][:2] == '!!':
        chatbot.Chatbot.get_response(new_message[2:len(new_message)])
    query(url, data['message'])
    
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )