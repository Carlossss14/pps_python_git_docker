import random

def frotar(n_frases: int = 1) -> list():
    frases = []

    # Leer las frases desde el fichero de texto
    with open("frases.txt", "r", encoding="utf-8") as f:
        todas = [linea.strip() for linea in f if linea.strip()]

    # Si piden más frases de las que hay, repetimos aleatoriamente
    for _ in range(n_frases):
        frases.append(random.choice(todas))

    return frases
