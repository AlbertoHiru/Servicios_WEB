#desde la librería flask importamos la clase Flask
from flask import Flask

#desde flaskrestful importamos la clase Api y Resource
from flask_restful import Api, Resource

#vamos a crear un objeto de la clase tipo Flask
app = Flask(__name__)

#creamos un objeto de la clase Api y como argumento le pasamos el objeto app
#------------------------------------------------------------------------------
#el parametro/argumento que espera recibir es el objeto de flask
api = Api(app)

#la API sera el programa que se cominique con el dispositivo fisico
#vamos a crear una clase que herede de Resource
class HelloWorld(Resource):
    #definimos el metodo get
    def get(self):
        return {'hello': 'world'}
    
class PantallaInicio(Resource):
    def get(self):
        return 'Bienvenido a la pantalla de inicio'

#Quiero que pueda acceder a este recursoa traves de una URL
#1. el recurso que va a ejecutar
#2. la URL a la que va a estar asociado ese recurso
api.add_resource(HelloWorld, '/hello')

#se le conoce como la ruta de inicio
api.add_resource(PantallaInicio, '/')

#------------------------------------------------------------------------------







#del objeto app ejecutamos el metodo run

app.run(port=8080, debug=True)