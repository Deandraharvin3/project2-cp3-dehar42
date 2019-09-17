import os
import flask, flask_socketio, flask_sqlalchemy

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Deandra:Dajah312!@localhost/postgres'  
db = flask_sqlalchemy.SQLAlchemy(app)

@app.route('/')
def hello():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    print('someone connected')
    
    flask_socketio.emit('update', {
        'data': 'Got your connection!'
    })
    
socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)