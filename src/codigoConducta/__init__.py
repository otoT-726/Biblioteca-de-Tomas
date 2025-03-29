def buscarReglas(rules, palabra):
    """Dado un código de conducta para un servidor de Discord: Solicite una palabra clave al usuario e imprima todas las reglas que la contengan."""
    reglas = rules.split(".")
    text= ""
    for i in reglas:
        if palabra in i:
            text += i + "\n"
    if(text != None and text != ""):
        text = "Las reglas que contienen la palabra son: " + text
    else:
        text = "No se encontraron reglas que contengan la palabra."
    return text
