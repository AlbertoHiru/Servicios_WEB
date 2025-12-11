from flask_restful import Resource
#los recursos de mi servidor web
from flask import make_response, render_template


#la API sera el programa que se cominique con el dispositivo fisico
#vamos a crear una clase que herede de Resource
class HelloWorld(Resource):
    #definimos el metodo get
    def get(self):
        return {'hello': 'world'}
    
class PantallaInicio(Resource):
    def get(self):
        contenido = render_template('index.html')
        #renderizamos el contenido del archivo index.html

        #retornamos el contenido renderizado
        return make_response() 

    
class Despedida(Resource):
    def get(self):
        return 'Gracias por visitarnos, hasta pronto!'

#podemos crear mas clases que hereden de Resource
#cada clase sera un recurso diferente de nuestra API    
    