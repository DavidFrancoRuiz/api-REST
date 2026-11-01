from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {
            "status": "success",
            "mensaje": "¡Hola! Mi API REST está funcionando en AWS con CodePipeline",
            "autor": "Andres, Camilo, David",
        }
    )


@app.route("/saludo/<nombre>", methods=["GET"])
def saludar(nombre):
    return jsonify({"mensaje": f"¡Hola, {nombre}! Bienvenido a mi API."})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"estado": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
