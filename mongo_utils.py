from pymongo import MongoClient
import random

# -----------------------------
# 1. Instanciación
# -----------------------------
from pymongo import MongoClient

def instanciar(host="mongo-bayeta", puerto=27017):
    cliente = MongoClient(f"mongodb://{host}:{puerto}/")
    bd = cliente["bayeta"]
    coleccion = bd["frases_auspiciosas"]
    return cliente, coleccion

# -----------------------------
# 2. Inicialización
# -----------------------------
def inicializar(ruta_fichero="frases.txt"):
    cliente, coleccion = instanciar()

    if coleccion.count_documents({}) == 0:
        with open(ruta_fichero, "r", encoding="utf-8") as f:
            datos = [{"frase": linea.strip()} for linea in f if linea.strip()]
        coleccion.insert_many(datos)

    cliente.close()

# -----------------------------
# 3. Consulta
# -----------------------------
def consultar(n_frases: int):
    cliente, coleccion = instanciar()
    frases = list(coleccion.aggregate([{"$sample": {"size": n_frases}}]))
    cliente.close()
    return [f["frase"] for f in frases]
