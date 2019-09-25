import os
import flask, flask_socketio, flask_sqlalchemy, psycopg2

import models

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

    
conn_string = "host='localhost' dbname='postgres' user='dee' password='deandra3'"

conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
 
	# execute our Query
cursor.execute("SELECT * FROM message")
 
	# retrieve the records from the database
records = cursor.fetchall()
print(records)

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
def query():
    cursor.execute("SELECT * FROM message")
    records = cursor.fetchall()
    return(records)
    
@socketio.on('new message')
def on_new_number(data):
    print(("Got an event for new number with data:"), data)
    # rand_number = data['message']
    messages = models.Message.query.all()
    chat = [m.text for m in messages]
    postgres_insert_query = """ INSERT INTO message (ID, TEXT) VALUES (%s, %s)"""
    record_to_insert = (len(chat)+1, data['message'])
    cursor.execute(postgres_insert_query, record_to_insert)

    conn.commit()
    update_records = query()
    socketio.emit('message received', {
        'message': update_records
    },
    callback=index())

if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )