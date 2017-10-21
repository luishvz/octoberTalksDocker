import datetime
from .. import db


class User(db.Model):
    __tablename__ = "users"

    """
    Atributes:
        id - <number>
        username - <string>
        email - <string>
        active - <boolean>
        created - <datetime>
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    active = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.utcnow()

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at
        }
