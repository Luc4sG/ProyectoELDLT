import requests
from bs4 import BeautifulSoup

# Make a request to the page and get the response content
url = 'https://sysacadweb.frre.utn.edu.ar/'
response = requests.get(url)
content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Look for a CSRF token field in the form
csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})

if csrf_token is not None:
    print('CSRF token found:', csrf_token['value'])
else:
    print('No CSRF token found')