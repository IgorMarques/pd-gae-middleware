from google.appengine.ext import db

from book import Book

import urllib

class Library:

  @staticmethod 
  def add_book(self, b_name, b_quantity):

    b = Book(name= b_name, quantity= int(b_quantity))

    urllib.unquote(b.name)

    self.response.write("> Voce cadastrou o livro: " + b.name  + " com "+ str(b.quantity))

    b.put()

  @staticmethod 
  def get_books(self):
    books = db.GqlQuery("SELECT * FROM Book")

    self.response.write("LIVRO    |   QUANTIDADE<br/>")

    for b in books:
      self.response.write("- "+b.name +" ----- " + str(b.quantity) + "<br/>")

    self.response.write("<br/>")

  @staticmethod
  def lend_book(self, book_name):
    books = db.GqlQuery("SELECT * FROM Book WHERE name = :1", book_name)

    for b in books:
      b.quantity = int( int(b.quantity) -1 )
      b.put()
      self.response.write("> A quantidade do livro " + b.name +  " eh: " + str(b.quantity)) 

  @staticmethod
  def return_book(self, book_name):
    books = db.GqlQuery("SELECT * FROM Book WHERE name = :1", book_name)

    for b in books:
      b.quantity = int( int(b.quantity) +1 )
      b.put()
      self.response.write("> A quantidade do livro " + b.name + " eh: " +  str(b.quantity))

  @staticmethod
  def delete_book(self, book_name):

    books = db.GqlQuery("SELECT * FROM Book WHERE name = :1", book_name)
    for b in books:
      b.delete()

    self.response.write("> Voce apagou o livro " + book_name +"do banco!")

  @staticmethod
  def delete_all(self):

    books= db.GqlQuery("SELECT * FROM Book")
    for b in books:
      b.delete()

    self.response.write("> Voce apagou o banco!<br/>")
