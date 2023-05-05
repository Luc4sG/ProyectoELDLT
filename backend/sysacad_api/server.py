import requests
from bs4 import BeautifulSoup


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
        return response
    
    #Extraer los datos de una tabla
    def _data_from_tables(self,bs_html,keys):
        data = []
        for tr in bs_html('tr'):
            tds={}
            i=0
            for td in tr('td'):
                if keys[i] == 'Inasistencias':
                    link = td.find('a').get('href')
                    tds[keys[i]] = link 
                else:
                    tds[keys[i]] = td.getText()
                i+=1
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

        print(login_data)
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
        data = self._data_from_tables(html,keys)
        for examen in data:
            if examen['Nota'] in {"uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "Ausen."}:
                examen['Nota'] = {
                    "uno": 1,
                    "dos": 2,
                    "tres": 3,
                    "cuatro": 4,
                    "cinco": 5,
                    "seis": 6,
                    "siete": 7,
                    "ocho": 8,
                    "nueve": 9,
                    "diez": 10,
                    "Ausen.": None
                }[examen['Nota']]
                
            
            if examen['Codigo'] and examen['Codigo'].isdigit():
                examen['Codigo'] = int(examen['Codigo'])        
            
        return data

    # def get_inasistencias(self,link): #TODO: Ejecutar solo cuando se pida para una sola materia
    #     data={}
    #     response = self._get(link)
    #     html = BeautifulSoup(response.content, 'html.parser')

    #     #Parsear la tabla de inasistencias
    #     keys = (    'Fecha', 
    #                 'Justificada' 
    #             )
    #     data['inasistencias'] = self._data_from_table(html,keys)
    #     for inasistencia in data['inasistencias']:
    #         inasistencia['fecha'] = dateparser.parse(inasistencia['fecha'])
    def get_inasistencias(self,link,materia):
        data={}
        
        return data


    
        

    def get_cursando(self):
        data={}
        response=self._get(self.url['cursado'])
        html = BeautifulSoup(response.content, 'html.parser')

        #Parsear la tabla de cursado
        keys = (    'Año',
                    'Materia',
                    'Comisión',
                    'Horarios',
                    'Notas',
                    'Condición',
                    'Obs.',
                    'Inasistencias' )
        data['cursando'] = self._data_from_tables(html,keys)
       
        
        return data
    

