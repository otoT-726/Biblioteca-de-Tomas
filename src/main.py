#Aclaracion: Se que los imports se ponen al inicio del programa pero los hice asi para que se pueda buscar mas facil la funcion que se necesita.



#Ejercicio 1 :

from chequearZen import chequear

zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
        """

print(chequear(zen))


#Ejercicio 2 :

from devolverMayorTitulo import devolverMayor

titulos =  [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]

print(devolverMayor(titulos))


#Ejercicio 3 :

from codigoConducta import buscarReglas

rules = """Respeta a los demás. No se permiten insultos ni lenguaje
ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores.
"""


pal = input("Ingresa la palabra buscada: ")
print(buscarReglas(rules, pal))


#Ejercicio 4 :

from validarUsuario import validar_usuario

clave = input("Ingrese el nombre de usuario: ")
print(validar_usuario(clave))


#Ejercicio 5 :

from reactTime import tiempo_reaccion

time = int(input("Ingrese el tiempo de reaccion en milisegundos: "))
print(tiempo_reaccion(time))

#Ejercicio 6 :