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

    #1. URL_fetch====================================================

    Register.register(self)

    self.response.set_status(200)

    self.response.write("App no Ar - Solicitacao Recebida<br/>")

    #2. E-mail=======================================================

    user_address = "igormarquessilva@gmail.com"
    subject = "Solicitacao via Middleware"
    body = "Sua solicitacao foi feita com sucesso. O aluno que fez esse web service merece um 10."

    Mailer.send_mail(self, user_address, subject, body)

  def post(self):
    params = decode(self.request.body)

    b = Book(params["name"], params["qtd"])

    self.response.write(b.name + b.quantity)

    b.put()




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/igor-app-id/hue', AppHandler)
], debug=True)


