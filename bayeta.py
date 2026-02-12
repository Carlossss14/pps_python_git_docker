import random

def frotar(n_frases: int = 1) -> list():
    frases = []
    with open("frases.txt", "r", encoding="utf-8") as f:
        todas = [linea.strip() for linea in f if linea.strip()]
    for _ in range(n_frases):
        frases.append(random.choice(todas))
    return frases
