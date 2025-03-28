def chequearZen(zen):
    """Imprime todas las lineas del zen de python cuya segunda palabra empieza con vocal."""
    vocal = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    lista_zen= zen.splitlines()
    text = ""
    for i in lista_zen:
        palabra  = i.split(" ")[1]
        if palabra.startswith(vocal):
            text += i + "\n"
    return text