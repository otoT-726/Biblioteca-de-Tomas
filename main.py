import string
import random

print('Generador de claves! ')

chars = string.ascii_letters + string.digits + string.punctuation
leng = int(input('Ingrese la longitud de su contraseña. '))
password = ''

for _ in range(leng):
    password = password + random.choice(chars)

print('La clave generada es: ', password)
