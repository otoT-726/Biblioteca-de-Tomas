def tiempo_reaccion(tiempo):
    """ Ingresa el tiempo de reaccion en milisegundos y devuelve una cadena que indica si es rapido, lento o normal."""
    if(tiempo < 200):
        return "Rapido"
    elif tiempo > 500:
        return "Lento"
    else:
        return "Normal"