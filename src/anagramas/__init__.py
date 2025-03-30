from collections import Counter
def anagramas(palabra1, palabra2):
    """Determine si dos palabras ingresadas son anagramas (contienen las mismas letras endiferente orden)."""
    counterpal1 = Counter(palabra1.lower())
    counterpal2 = Counter(palabra2.lower())
    return counterpal1 == counterpal2
