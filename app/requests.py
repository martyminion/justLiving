import urllib.request,json
from .models import Quote

def get_quotes():
  '''
  gets the quotes from the url
  '''
  quote_url = "http://quotes.stormconsultancy.co.uk/random.json"
  with urllib.request.urlopen(quote_url) as url:
    get_quote_data = url.read()
    get_quote_response = json.loads(get_quote_data)

    if get_quote_response:
      id = get_quote_response.get('id')
      author = get_quote_response.get('author')
      quote = get_quote_response.get('quote')
    
  new_quote = Quote(id,author,quote)

  return new_quote