from flask_restful import Resource
#los recursos de mi servidor web
from flask import make_response, render_template, request , redirect

cliente_db = None  # Variable global para almacenar el cliente de la base de datos
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
        return make_response(contenido) 




class Despedida(Resource):
    def get(self):

        print('Esto es un texto de prueba')
        return 'Adios'
class login(Resource):

    def get(self):
        return make_response(render_template('login.html'))

    def post(self):
        datos = request.form.to_dict()
        print("Datos recibidos login:", datos)

        resultado = (
            cliente_db
            .table("usuarios")
            .select("*")
            .eq("correo", datos["correo"])
            .eq("password", datos["password"])
            .execute()
        )

        if resultado.data:
            # login correcto
            return redirect('/hub')

        # login incorrecto → regresa al login
        return make_response(render_template('login.html'))
        

class crear(Resource):
    def get(self):
        contenido = render_template('crear.html')
        return make_response(contenido)
    def post(self):
        datos = request.form.to_dict()  
        print("Datos recibidos para crear cuenta:", datos)
        cliente_db.table("usuarios").insert(datos).execute()
        print("Cuenta creada exitosamente")
        return redirect('/hub')
        
    


class hub(Resource):
    def get(self):
        contenido = render_template('hub.html')
        return make_response(contenido)
    

#podemos crear mas clases que hereden de Resource
#cada clase sera un recurso diferente de nuestra API    
    