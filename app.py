#app.py
import os
import flask, flask_socketio, json, yelpAPI
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
    # user_count += 1
    messages = models.Message.query.all()
    chat = [m.text + "\n" for m in messages]
    flask_socketio.emit('update', {
        'data': 'Got your connection!',
        'previous_messages': chat
    })

@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')
    
    flask_socketio.emit('disconnected', {
        'data': 'Disconnected'
    })

@socketio.on('new message')
def on_message(data):
    url = False
    response = ''
    get_business_url = ''
    print("Got an event for new number with data")
    new_message = models.Message(data['message'])
    models.db.session.add(new_message)
    models.db.session.commit()
    
    # Getting the username and profile picture from Google login
    user_data = json.dumps(data['user_data'])
    loaded_data = json.loads(user_data)
    Google_username = str(loaded_data['profileObj']['name'])
    Google_profile = str(loaded_data['profileObj']['imageUrl'])
    
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
        
        if response.isalpha() == False:
            yelp_response = yelpAPI.YelpBusinessId(response)
            # response = json.dumps(yelp_response['name'], cls=AlchemyEncoder)
            response = yelp_response['name']
            print(response)
            get_business_url = yelp_response['url']
            print("Yelp response ", response, get_business_url)

    query(url, data['message'], response, get_business_url, Google_username, Google_profile)
    
    
def query(isurl, message, response, yelp_business, username, profile_picture):
    if response != '':
        print('Recieved response from chatbot')
        new_message = models.Message(response)
        models.db.session.add(new_message)
        models.db.session.commit()
    print('Querying all the messages in the database')    
    messages = models.Message.query.all()
    chat = [m.text + '\n\n' for m in messages]
    socketio.emit('message received', {
        'chat': chat,
        'message': message,
        'url': isurl,
        'username': username,
        'profilePic': profile_picture,
        'bot_response': response,
        'yelp_url': yelp_business
    })

        
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )