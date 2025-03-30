import random
import string
from datetime import datetime

def generar_clave(usuario):
    """Genera un código de descuento aleatorio para un usuario en base a su nombre, la fecha
       actual y el resto son números o letras aleatorias. Validar que el nombre de usuario no
       exceda los 15 caracteres."""
    if len(usuario) < 15:
        tiempo_actual = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day)
        clave = usuario.upper() + "-" + tiempo_actual + "-"
        for i in range(30-len(clave)):
            clave += random.choice(string.ascii_uppercase + string.digits)
        return clave
    else:
        print("Nombre de usuario demasiado largo")