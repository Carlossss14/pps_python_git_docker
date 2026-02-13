from flask import Flask, jsonify, request
from bayeta import frotar, insertar
from mongo_utils import inicializar

# Inicializar Mongo al arrancar
inicializar()

app = Flask(__name__)

@app.route("/")
def hola():
    return "<h1>Hola, mundo</h1>"

@app.route("/frotar/<int:n_frases>")
def endpoint_frotar(n_frases):
    frases = frotar(n_frases)
    return jsonify(frases)

@app.route("/frotar/add", methods=["POST"])
def endpoint_add():
    data = request.get_json()

    if not data or "frases" not in data:
        return jsonify({"error": "Debes enviar un JSON con el campo 'frases'"}), 400

    insertar(data["frases"])
    return jsonify({"status": "ok", "insertadas": len(data["frases"])}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
