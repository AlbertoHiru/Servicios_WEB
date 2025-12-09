#rutas de acceso a los recursos de mi servidor web

from recursos import *


def crear_rutas(api):
        #Quiero que pueda acceder a este recursoa traves de una URL
    #1. el recurso que va a ejecutar
    #2. la URL a la que va a estar asociado ese recurso
    api.add_resource(HelloWorld, '/hello')

    #se le conoce como la ruta de inicio
    api.add_resource(PantallaInicio, '/')

    api.add_resource(Despedida, '/despedida')


#