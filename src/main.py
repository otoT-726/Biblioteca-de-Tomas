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

#Ejercicio 6 : Dadas varias descripciones de streams en Twitch, cuente cuántas menciones hay de
#              "entretenimiento", "música" y "charla".

from buscarPalabras import buscar_palabras

descriptions = [
"Streaming de música en vivo con covers y composiciones",
"Charla interactiva con la audiencia sobre series y películas",
"Jugamos a juegos retro y charlamos sobre su historia",
"Exploramos la mejor música de los 80s y 90s",
"Programa de entretenimiento con noticias y curiosidades del mundo gamer",
"Sesión de charla con invitados especiales del mundo del streaming",
"Música en directo con improvisaciones y peticiones del chat",
"Un espacio para charlar relajada sobre tecnología y cultura digital",
"Exploramos el impacto de la música en los videojuegos clásicos"]

buscar_palabras(descriptions)


#Ejercicio 7 : Genere un código de descuento aleatorio para un usuario en base a su nombre, la fecha actual y el resto deben ser números o letras aleatorias.
#              El código debe tener una longitud de 30 caracteres, todas las letras deben ser mayúsculas.
#              El usuario debe ingresarse por teclado y debe validar que no exeda los 15 caracteres.

from generarClaves import generar_clave

usuario = input("Ingrese el nombre de usuario: ")
if(generar_clave(usuario) != None):
    print("Codigo de descuento: " + generar_clave(usuario))


#Ejercicio 8 : Determine si dos palabras ingresadas son anagramas (contienen las mismas letras en diferente orden).

from anagramas import anagramas

palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

if anagramas(palabra1, palabra2):
    print("Son anagramas")
else:
    print("No son anagramas")


#Ejercicio 9 : Limpia los datos de una lista dada.

from limpiarDatos import clean_data

clients = [
" Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "",
" Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
"luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA TORRES",
" ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURA RAMOS",
"carlos mendes", "RICARDO FERNÁNDEZ ", " Laura ramos", "CARLOS MENDES",
"alejandro gonzález", " ALEJANDRO GONZÁLEZ ", "Patricia Vega",
"patricia VEGA", "Andrés Ocampo", " andrés ocampo", "Monica Herrera",
"MONICA HERRERA ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
"SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
"Damián Castillo ", None, "", " "
]

lista_limpia = clean_data(clients)
print(lista_limpia)

#COMENTARIO: El unico dato que no pude limpiar es la tilde de "María Martinez".