from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        edad = request.form.get("edad", "").strip()

        if not nombre:
            return "❌ El nombre es obligatorio", 400

        try:
            edad_numero = int(edad)
        except ValueError:
            return "❌ La edad debe ser un número", 400

        if edad_numero < 0 or edad_numero > 120:
            return "❌ La edad debe estar entre 0 y 120", 400

        return f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Datos aceptados</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #f4f7fb;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    margin: 0;
                }}

                .card {{
                    background: white;
                    width: 90%;
                    max-width: 420px;
                    padding: 35px;
                    border-radius: 20px;
                    text-align: center;
                    box-shadow: 0 10px 30px rgba(0,0,0,.12);
                }}

                .ok {{
                    font-size: 50px;
                }}

                h1 {{
                    color: #1f2937;
                }}

                p {{
                    color: #4b5563;
                    font-size: 18px;
                }}

                a {{
                    display: inline-block;
                    margin-top: 20px;
                    padding: 12px 22px;
                    background: #2563eb;
                    color: white;
                    text-decoration: none;
                    border-radius: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <div class="ok">✅</div>
                <h1>Datos aceptados</h1>
                <p><strong>Nombre:</strong> {nombre}</p>
                <p><strong>Edad:</strong> {edad_numero}</p>
                <a href="/">Regresar</a>
            </div>
        </body>
        </html>
        """

    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Laboratorio de pruebas</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #2563eb, #7c3aed);
                min-height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }

            .card {
                background: white;
                width: 100%;
                max-width: 450px;
                padding: 35px;
                border-radius: 22px;
                box-shadow: 0 15px 40px rgba(0,0,0,.25);
            }

            h1 {
                margin-top: 0;
                color: #111827;
                text-align: center;
            }

            .subtitle {
                text-align: center;
                color: #6b7280;
                margin-bottom: 30px;
            }

            label {
                display: block;
                margin-bottom: 8px;
                color: #374151;
                font-weight: bold;
            }

            input {
                width: 100%;
                padding: 13px;
                margin-bottom: 20px;
                border: 1px solid #d1d5db;
                border-radius: 10px;
                font-size: 16px;
                outline: none;
            }

            input:focus {
                border-color: #2563eb;
            }

            button {
                width: 100%;
                padding: 14px;
                border: none;
                border-radius: 10px;
                background: #2563eb;
                color: white;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
            }

            button:hover {
                background: #1d4ed8;
            }

            .footer {
                text-align: center;
                margin-top: 20px;
                font-size: 13px;
                color: #9ca3af;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>🧪 Laboratorio de pruebas</h1>

            <p class="subtitle">
                Formulario de validación con Flask
            </p>

            <form method="POST">

                <label for="nombre">Nombre</label>
                <input
                    type="text"
                    id="nombre"
                    name="nombre"
                    placeholder="Escribe tu nombre"
                    required
                >

                <label for="edad">Edad</label>
                <input
                    type="number"
                    id="edad"
                    name="edad"
                    placeholder="Escribe tu edad"
                    min="0"
                    max="120"
                    required
                >

                <button type="submit">
                    Enviar datos
                </button>

            </form>

            <div class="footer">
                Laboratorio Flask • Validación del lado servidor
            </div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
