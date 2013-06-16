from google.appengine.ext import db

class Book(db.Model):

  name = db.StringProperty(required=True)
  quantity = db.StringProperty(required=True)


  def list_books(self):
    books = db.GqlQuery("SELECT * FROM Book")

    for e in books:
      self.response.write(e.name + e.quantity)
