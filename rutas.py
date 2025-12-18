#rutas de acceso a los recursos de mi servidor web

from recursos import HelloWorld, PantallaInicio, Despedida, login, crear, hub



def crear_rutas(api):
        #Quiero que pueda acceder a este recursoa traves de una URLclass Despedida(Resource):
    def get(self):
        print("adios")
        return 'Gracias por visitarnos, hasta pronto!'
    #1. el recurso que va a ejecutar
    #2. la URL a la que va a estar asociado ese recurso
    api.add_resource(HelloWorld, '/hello')

    #se le conoce como la ruta de inicio
    api.add_resource(PantallaInicio, '/')

    api.add_resource(Despedida, '/despedida')

    api.add_resource(login, '/login')

    api.add_resource(crear, '/crear') 

    api.add_resource(hub, '/hub') 






    #podemos agregar mas rutas a otros recursos
    #api.add_resource(NombreRecurso, '/ruta')
    