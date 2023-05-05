from server import SessionSysacad

session = SessionSysacad('https://sysacadweb.frre.utn.edu.ar/')
session.login('25446','Coco1752')
print(session.get_examenes())