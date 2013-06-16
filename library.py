from google.appengine.ext import db

from book import Book

class Library:

  @staticmethod 
  def add_book(self, b_name, b_quantity):

    b = Book(name= b_name, quantity= int(b_quantity))

    self.response.write(b.name + str(b.quantity))

    b.put()

  @staticmethod 
  def get_books(self):
    books = db.GqlQuery("SELECT * FROM Book")

    for b in books:
      self.response.write(b.name + str(b.quantity))

  @staticmethod
  def lend_book(self, book_name):
    books = db.GqlQuery("SELECT * FROM Book")

    for b in books:
      b.quantity = int( int(b.quantity) -1 )
      b.put()
      self.response.write("> A quantidade do livro" + b.name +  " eh: " + str(b.quantity)) 

  @staticmethod
  def return_book(self, book_name):
    books = db.GqlQuery("SELECT * FROM Book")

    for b in books:
      b.quantity = int( int(b.quantity) +1 )
      b.put()
      self.response.write("> A quantidade do livro" + b.name + " eh: " +  str(b.quantity))

  @staticmethod
  def delete_book(self, book_name):

    books = db.GqlQuery("SELECT * FROM Book WHERE name = :1", book_name)
    for b in books:
      b.delete()

    self.response.write("> Voce apagou o livro " + book_name +"do banco!")

  @staticmethod
  def delete_all(self):
    self.response.write("> Voce apagou o banco!")
    books= db.GqlQuery("SELECT * FROM Book")
    for b in books:
      b.delete()

