#desde la librería flask importamos la clase Flask
from flask import Flask
#desde flaskrestful importamos la clase Api y Resource
from flask_restful import Api, Resource
from rutas import crear_rutas
from extensiones import inicializar_db
import recursos

recursos.cliente_db = inicializar_db()


#------------------------------------------------------------------------------

#vamos a crear un objeto de la clase tipo Flask
app = Flask(__name__)

#creamos un objeto de la clase Api y como argumento le pasamos el objeto app
#------------------------------------------------------------------------------
#el parametro/argumento que espera recibir es el objeto de flask
api = Api(app)

#------------------------------------------------------------------------------


# Registrar las rutas de la API usando la función crear_rutas
crear_rutas(api)
#------------------------------------------------------------------------------



#------------------------------------------------------------------------------
#del objeto app ejecutamos el metodo run


app.run(port=8080, debug=True)
#el metodo run recibe dos parametros opcionales
#port: el puerto en el que se va a ejecutar la aplicación
#debug: si se pone en True, cada vez que se haga un cambio en el código
#se reiniciará automáticamente la aplicación
#podemos agregar mas rutas a otros recursos
#api.add_resource(NombreRecurso, '/ruta')
#el parametro/argumento que espera recibir es el objeto de flask

#Datos recibidos para crear cuenta: {'nombre': 'jesus', 'correo': 'jesus@correo.com', 'password': 'hola', 'confirmar_password': 'hola'}

#contraseña supabase :  w2oooBJrzelzNIeI