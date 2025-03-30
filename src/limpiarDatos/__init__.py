def clean_name(name):
    if name == None or name == "":
        return None
    return name.strip().capitalize()

def clean_data(clientes):
    lista_limpia = []
    for i in clientes:
        if i != None and i != "" and i != " ":
            i = i.strip().split(" ")
            if(clean_name(i[0]) + " " + clean_name(i[1]) not in lista_limpia):
                lista_limpia.append(clean_name(i[0]) + " " + clean_name(i[1]))
    return lista_limpia