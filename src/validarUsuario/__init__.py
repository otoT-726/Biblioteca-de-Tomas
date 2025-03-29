import string

def validar_usuario(clave):
    if(len(clave) < 5):
        return "La clave no es válida, debe tener al menos 5 caracteres."
    validos = string.ascii_letters + string.digits
    mayus = False
    num = False
    valido = False
    for i in clave:
        if i in string.ascii_uppercase:
            mayus = True
        else:
            if i in string.digits:
                num = True
        if(i not in validos):
            return "La clave no es válida, contiene caracteres no permitidos."
    if(mayus and num):
        return "Clave validada."
    else:
        return "La clave no es válida, debe contener al menos una letra mayúscula y un número."