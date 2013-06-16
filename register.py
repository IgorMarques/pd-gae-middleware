from google.appengine.api import capabilities
from google.appengine.api import urlfetch
import urllib2
import urllib

class Register:

  @staticmethod 
  def register(self):

    if capabilities.CapabilitySet('urlfetch').is_enabled():
      self.response.write("> UrlFetch ok! Registrando App! \n <br/>")

      #cadastrando aplicacao no lookup
      form_fields = {
        "endpoint": "igor-pd-app.appspot.com",
        "id": "igor-app-id"
      }

      url = "http://lookuppd.appspot.com/objects/add"
      
      form_data = urllib.urlencode(form_fields)

      result= urlfetch.fetch(url=url,
      payload=form_data,
      method=urlfetch.POST,
      headers={'Content-Type': 'application/x-www-form-urlencoded'})

    else:
      self.response.write("> Servico UrlFetch down! App nao registrada!")
    