from baseparser import BaseParser
from goose import Goose

class GooseParser(BaseParser):
  def __init__(self, url):
      self.url = url
      g = Goose()
      try:
          self.html = g.extract(url=self.url)
      except urllib2.HTTPError as e:
          if e.code == 404:
              self.real_article = False
              return
          raise
      self._parse(self.html)

  def _parse(self, html):
    self.title = html.title
    self.body = html.cleaned_text
    self.date = ''
    self.byline = ''