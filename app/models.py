from datetime import datetime

from . import db

SHORT_LEN = 6

class URLmodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255))
    short = db.Column(db.String(SHORT_LEN), unique=True)
    visits = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now())
