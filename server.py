import requests
from bs4 import BeautifulSoup
import time
from dotenv.main import load_dotenv
import os

load_dotenv()

class SessionSysacad(object):

    #Excepciones 
    class AuthenticationError(Exception):
        pass
    
    class OperationError(Exception):
        pass

    #URLs a las que puede acceder la API
    url = {
        'default': 'Alumnos/menu/',
        'examenes': 'Alumnos/Examenes/',
        'cursado': 'Alumnos/Cursado/',
        'login': ''
        #posibles rutas a futuro:
        #correlatividades
        #certif alumno regular
    }

    #Constructor
    def __init__(self, url_base, session=None):
        self.url_base = url_base
        if session:
            assert isinstance(session, requests.Session), 'session debe ser una instancia de requests.Session'
            self.session = session 
        else:
            self.session = requests.Session()

    def _get(self,ext_url,data=None):
        url = self.url_base + ext_url
        response = self.session.get(url,data=data)
    
    #Extraer los datos de una tabla
    def _data_from_table(bs_html, keys):
        data = []
        for tr in bs_html('tr'):
            tds = {}
            i = 0
            for td in tr('td'):
                tds[keys[i]] = td.getText()
                i += 1
            data.append(tds)
        del data[0]
        return data

    # def _is_login_page(self, text):
	# 	html = BeautifulSoup(text, 'lxml')
	# 	if html.title.string == u'Ingreso Alumnos al SYSACAD' or html('p', attrs={'class': "textoError"}):
	# 		return True
	# 	return False
        
    def login(self, legajo, password):

        response = self._get(self.url['login'])
        html = BeautifulSoup(response.content, 'html.parser')
        csrf_token = html.find('input', {'name': 'csrfmiddlewaretoken'}).get("value")
        
        print(response)

        login_data = {
        'csrfmiddlewaretoken': csrf_token,
        'radio': 'A', # Assuming the user is always an "Alumno"
        'username': legajo,
        'password': password,
        'submit': 'Acceder',
        }

        response = self.session.post(self.url_base, data=login_data)
        print(response)

    def get_examenes(self):
        data={}
        response = self._get(self.url['examenes'])
        html = BeautifulSoup(response.content, 'html.parser')

        #Parsear la tabla de examenes
        keys = (    'Fecha', 
                    'Materia', 
                    'Nota', 
                    'Especialidad', 
                    'Plan', 
                    'Codigo'
                )
        data['examenes'] = self._data_from_table(html,keys)
        for examen in data['examenes']:
            examen





