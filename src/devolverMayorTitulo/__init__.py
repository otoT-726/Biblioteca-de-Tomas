def devolverMayor(lista):
    """ Devuelve el título más largo de una lista dada """
    
    max = 0
    for i in lista:
        cant = len(i)
        if cant > max:
            max = cant
            maxtitle = i
    return maxtitle