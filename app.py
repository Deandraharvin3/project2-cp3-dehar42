import os
import flask, flask_socketio, json
import models, chatbot
from rfc3987 import parse

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
 
@app.route('/')

def index():
    return flask.render_template("index.html")

socketio.emit('google keys', {
    'GoogleID': os.getenv("GOOGLE_ID"),
    'GoogleSecret': os.getenv("GOOGLE_SECRET")
})
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

# This is how you get the data from the Content.js Google login to save the username of the user logging in
@socketio.on('user signin')
def googleLogin(data):
    user_data = json.dumps(data['user'])
    loaded_data = json.loads(user_data)
    print('Recieved data: ' + str(loaded_data['profileObj']['name']))
    
@socketio.on('new message')
def on_new_number(data):
    url = False
    response = ''

    print(("Got an event for new number with data:"), data)
    new_message = models.Message(data['message'])
    models.db.session.add(new_message)
    models.db.session.commit()
    
    #checking if the message is a link
    try:
        parse(data['message'], rule='URI')
        print('Received a URL')
        url = True
    except:
        print('Message not URL')
        
    if data['message'][:2] == '!!':
        chat_message = data['message'] 
        bot_response = chatbot.Chatbot()
        print("Chatbot message: " + chat_message)
        response = bot_response.get_response(chat_message[2:])
        
    query(url, data['message'], response)
    
    
def query(isurl, new_message, response):
    messages = models.Message.query.all()
    chat = [m.text + '\n' for m in messages]
    socketio.emit('message received', {
        'chat': chat[0:len(chat)-1],
        'message': new_message,
        'url': isurl,
        'bot_response': response
    })
    
    
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )