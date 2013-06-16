from google.appengine.ext import db

class Book(db.Model):

  name = db.StringProperty(required=True)
  quantity = db.StringProperty(required=True)
