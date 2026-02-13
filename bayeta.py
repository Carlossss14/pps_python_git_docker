from mongo_utils import consultar, insertar as insertar_mongo

def frotar(n_frases: int = 1):
    return consultar(n_frases)

def insertar(frases: list):
    insertar_mongo(frases)
