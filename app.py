from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":

        nombre = request.form.get("nombre", "")
        edad = request.form.get("edad", "")

        try:
            edad_numero = int(edad)

            if edad_numero < 0 or edad_numero > 120:
                return "❌ Edad fuera de rango.", 400

        except ValueError:
            return "❌ La edad debe ser un número.", 400

        return f"✅ Datos aceptados: {nombre}, {edad_numero}", 200

    return """
    <h1>Laboratorio de pruebas</h1>

    <form method="POST">

        <label>Nombre:</label><br>
        <input type="text" name="nombre"><br><br>

        <label>Edad:</label><br>
        <input type="text" name="edad"><br><br>

        <button type="submit">Enviar</button>

    </form>
    """

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.enviaron.get("PORT", 5000)

