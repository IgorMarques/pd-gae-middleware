#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# -*- coding: utf-8 -*- 

from mailer import Mailer
from register import Register
from book import Book
from library import Library

import webapp2

class AppHandler(webapp2.RequestHandler):

    def get(self):
        self.response.set_status(200)
        self.response.write("Funcionou")

def decode(s):
    vector = s.split("&")

    params = {}

    for v in vector:
      aux = v.split("=")
      params[aux[0]] = aux[1]

    return params

class MainHandler(webapp2.RequestHandler):

  def get(self):

    Library.get_books(self)

    #1. URL_fetch====================================================

    Register.register(self)

    self.response.set_status(200)

    self.response.write("App no Ar - Solicitacao Recebida<br/>")

    #2. E-mail=======================================================

    user_address = "igormarquessilva@gmail.com"
    subject = "Solicitacao via Middleware"
    body = "Igor, alguém acessou sua aplicação. Vá conferir se ninguém zuou tudo!"

    Mailer.send_mail(self, user_address, subject, body)

  def post(self):
    params = decode(self.request.body)

    if (params ["request_type"] == "lend"): 
      Library.lend_book(self, params["book"])
    else:
      if(params["request_type"] == "return"):
        Library.return_book(self, params["book"])
      else:
        self.request.body("> Invalid operation!")

    

  def put(self):
    params = decode(self.request.body)

    Library.add_book(self, params["name"], params["qtd"])

  def delete(self):
    params = decode(self.request.body)

    Library.delete_book(self, params["name"])


app = webapp2.WSGIApplication([
    ('/igor-app-pd/library', MainHandler),
    ('/igor-app-id/hue', AppHandler)
], debug=True)


