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

from google.appengine.api import mail
from google.appengine.api import xmpp
from google.appengine.api import capabilities

import webapp2

class MainHandler(webapp2.RequestHandler):

  def get(self):
    #E-mail
    sender_address = "igormarquessilva@gmail.com"
    user_address = "igormarquessilva@gmail.com"
    subject = "Solicitacao via Middleware"
    body = "Sua solicitacao foi feita com sucesso. O aluno que fez esse web service merece um 10."

    self.response.write('Hello, webapp2 World!')

    print "hue"

    mail.send_mail(sender_address, user_address, subject, body)

    #Chat- Chat do Google nao suporta mais
    chat_message_sent = False
    msg = "Sua solicitacao foi feita com sucesso. O aluno que fez esse web service merece um 10."
    status_code = xmpp.send_message(user_address, msg)
    chat_message_sent = (status_code == xmpp.NO_ERROR)

    #capabilities
    if capabilities.CapabilitySet('mail').is_enabled():
      self.response.write('E-mail ta funfando!')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
