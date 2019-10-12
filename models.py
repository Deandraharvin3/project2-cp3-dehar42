# models.py
import flask_sqlalchemy, flask, flask_socketio, app


# app.app = app modules app variable
app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dee:deandra3@localhost/postgres'

db = flask_sqlalchemy.SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key
    text = db.Column(db.String(220))

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'modified_at': dump_datetime(self.modified_at),
           # This is an example how to deal with Many2Many relations
           'many2many'  : self.serialize_many2many
       }
    @property
    def serialize_many2many(self):
       """
       Return object's relations in easily serializable format.
       NB! Calls many2many's serialize property.
       """
       return [ item.serialize for item in self.many2many]
       
    def __init__(self, text):
        self.text = text
    def __repr__(self):
        return '<Message text: %s>' % self.text 