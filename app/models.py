from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy() 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save_user(self):
        db.session.add(self)
        db.session.commit()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String)
    img_url = db.Column(db.String)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, body, img_url, user_id):
        self.title = title
        self.body = body
        self.img_url = img_url
        self.user_id = user_id

class Pokemon():
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    abilities = db.Column(db.String, nullable=False)
    base_experience = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    special_attack = db.Column(db.String, nullable=False)
    sprites = db.Column(db.String, nullable=False)

    def __init__(self, name, abilities, base_experience, attack, defense, special_attack, sprites):
        self.name = name
        self.abilities = abilities
        self.base_experience = base_experience
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.sprites = sprites

    def savePoke(self):
        db.session.add(self)
        db.session.commit()

