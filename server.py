import requests
from bs4 import BeautifulSoup
import time
from dotenv.main import load_dotenv
import os

load_dotenv()

def scrape_authenticated_page(url, username, password):
    # Create a session object to persist the login cookies
    session = requests.session()

    # Make a GET request to the login page to get the CSRF token
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'}).get("value") 

   

    # Prepare the login data and submit the POST request
    login_data = {
        'csrfmiddlewaretoken': csrf_token,
        'radio': 'A', # Assuming the user is always an "Alumno"
        'username': username,
        'password': password,
        'submit': 'Acceder',
    }
    session.post(url, data=login_data)

    # Make a GET request to the page that requires authentication
    response = session.get('https://sysacadweb.frre.utn.edu.ar/Alumnos/Cursado/')
    soup = BeautifulSoup(response.content, 'html.parser')
    # Parse the content of the page and extract the data you need

    return soup

if __name__ == '__main__': 
    start = time.time()
    soup = scrape_authenticated_page('https://sysacadweb.frre.utn.edu.ar/', '25446', os.environ['PASSWORD'])
    # print all the response 
    # print(soup)
    end = time.time()
    print(end - start)