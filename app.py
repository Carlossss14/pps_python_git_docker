from flask import Flask, jsonify
from bayeta import frotar
from mongo_utils import inicializar

# Inicializar Mongo al arrancar el contenedor
inicializar()

app = Flask(__name__)

@app.route("/")
def hola():
    return "<h1>Hola, mundo</h1>"

@app.route("/frotar/<int:n_frases>")
def endpoint_frotar(n_frases):
    frases = frotar(n_frases)
    return jsonify(frases)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
