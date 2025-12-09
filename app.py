#desde la librería flask importamos la clase Flask
from flask import Flask
#desde flaskrestful importamos la clase Api y Resource
from flask_restful import Api, Resource
from rutas import crear_rutas

#vamos a crear un objeto de la clase tipo Flask
app = Flask(__name__)

#creamos un objeto de la clase Api y como argumento le pasamos el objeto app
#------------------------------------------------------------------------------
#el parametro/argumento que espera recibir es el objeto de flask
api = Api(app)

#------------------------------------------------------------------------------


# Registrar las rutas de la API usando la función crear_rutas
crear_rutas(api)

#del objeto app ejecutamos el metodo run

app.run(port=8080, debug=True)