from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from app import app
from . import db

class myprofile(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
    
    
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
        
    
    def generate_auth_token(self, expiration = 600):
        s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps({ 'id': self.id })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = myprofile.query.get(data['userid'])
        return user
        
    
    def is_authenticated(self):
        return True
        
        
    def is_active(self):
        return True
        
        
    def is_anonymous(self):
        return False
        
        
    def get_id(self):
        return unicode(self.userid)
        
        
    def __repr__(self):
        return '<User %r>' % self.userid


class mywish(db.Model):
    wishid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('myprofile.userid'))
    description_url = db.Column(db.String(500))
    
    
    def __init__(self, userid, description_url):
        self.userid = userid
        self.description_url = description_url