import os
import flask, flask_socketio,psycopg2

import models

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

conn_string = "host='localhost' dbname='postgres' user='dee' password='deandra3'"

conn = psycopg2.connect(conn_string)
 
# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
query_all = False
@app.route('/')

def index():
    messages = models.Message.query.all()
    chat = [m.text for m in messages]
    return flask.render_template("index.html")

@socketio.on('connect')
def on_connect():
    print('someone connected')
    flask_socketio.emit('update', {
        'data': 'Got your connection!',
        'previous_messages': query()
    })
    return query()

@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')
    
    flask_socketio.emit('update', {
        'data': 'Disconnected'
    })

def query():
    messages = models.Message.query.all()
    chat = [m.text for m in messages]
    return(chat)
    
def chat_bot_response(records, message):
    if message == '!! help':
        chatbot_message = 'try typing \"!! about\" or \"!! chat\" for me to respond'
    if message == '!! about':
        chatbot_message = 'Welcome to Deandra\'s chatbot where you can talk to anyone on here including me'
    if message == '!! chat':
        chatbot_message = 'I love talking to you chat anytime'
    
    postgres_insert_query = """ INSERT INTO message (ID, TEXT) VALUES (%s, %s)"""
    record_to_insert = (len(records)+1, chatbot_message)
    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit() 
    
@socketio.on('new message')
def on_new_number(data):
    print(("Got an event for new number with data:"), data)
    # rand_number = data['message']
    update_records = query()
    postgres_insert_query = """ INSERT INTO message (ID, TEXT) VALUES (%s, %s)"""
    record_to_insert = (len(update_records)+1, data['message'])
    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit() 
    
    if data['message'] == '!! help' or data['message'] == '!! chat' or data['message'] == '!! about':
        chat_bot_response(update_records, data['message'])
    
    socketio.emit('message received', {
        'message': query()
    },
    callback=index())
    
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )