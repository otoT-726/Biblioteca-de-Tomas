def buscar_palabras(descriptions):
    """Dadas varias descripciones de streams en Twitch, cuente cuántas menciones hay de
       "entretenimiento", "música" y "charla"."""
    entretenimiento = 0
    musica = 0
    charla = 0
    for i in descriptions:
        i = i.lower()
        if "entretenimiento" in i:
            entretenimiento += 1
        if "música" in i:
            musica += 1
        if "charla" in i:
            charla += 1
    print(f"Entretenimiento: {entretenimiento}, Música: {musica}, Charla: {charla}")