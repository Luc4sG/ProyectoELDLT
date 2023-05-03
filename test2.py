import requests
from bs4 import BeautifulSoup
import time
from dotenv.main import load_dotenv
import os
import dateparser

load_dotenv()

def _data_from_tables(bs_html,keys):
    data = []
    for tr in bs_html('tr'):
        tds={}
        i=0
        for td in tr('td'):
            if keys[i] == 'Inasistencias':
                link = td.find('a').get('href')
                tds[keys[i]] = link.strip('"')
            else:
                tds[keys[i]] = td.getText()
            i+=1
        data.append(tds)
    del data[0]
    return data

def get_inasistencias(link,session):
        data={}
        url='https://sysacadweb.frre.utn.edu.ar/'
        response = session.get(url+link)
        html = BeautifulSoup(response.content, 'html.parser')

        #Parsear la tabla de inasistencias
        keys = (    'Fecha', 
                    'Justificada' 
                )
        data['inasistencias'] = _data_from_tables(html,keys)
        for inasistencia in data['inasistencias']:
            inasistencia['fecha'] = dateparser.parse(inasistencia['fecha'])
        
        return data


                



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
    keys = (    'Año',
                    'Materia',
                    'Comisión',
                    'Horarios',
                    'Notas',
                    'Condición',
                    'Obs.',
                    'Inasistencias' )
    lista = _data_from_tables(soup,keys)
    for l in lista:
        l['Inasistencias'] = get_inasistencias(l['Inasistencias'],session)


    # Parse the content of the page and extract the data you need

    return soup

if __name__ == '__main__': 
    start = time.time()
    soup = scrape_authenticated_page('https://sysacadweb.frre.utn.edu.ar/', '25446', os.environ['PASSWORD'])
    # print all the response 
    keys = (    'Año',
                    'Materia',
                    'Comisión',
                    'Horarios',
                    'Notas',
                    'Condición',
                    'Obs.',
                    'Inasistencias' )
    lista = _data_from_tables(soup,keys)
    print(lista)
    end = time.time()
    print(end - start)


        
