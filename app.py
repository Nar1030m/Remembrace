from flask import Flask, request, redirect, url_for, render_template_string
import os

app = Flask(__name__)

# Comentarios guardados temporalmente mientras la aplicación está funcionando
comentarios = []


HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Remembrace</title>

    <style>

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Georgia, 'Times New Roman', serif;
            background: #f5f1eb;
            color: #3d3833;
        }

        header {
            background: linear-gradient(
                135deg,
                #5b4b45,
                #8c7468
            );

            color: white;
            text-align: center;
            padding: 60px 20px;
        }

        header h1 {
            font-size: 48px;
            margin: 0 0 10px;
            letter-spacing: 3px;
        }

        header p {
            font-size: 19px;
            margin: 0;
            opacity: 0.95;
        }

        .contenedor {
            width: 92%;
            max-width: 1100px;
            margin: 40px auto;
        }

        .introduccion {
            text-align: center;
            max-width: 750px;
            margin: 0 auto 45px;
        }

        .introduccion h2 {
            font-size: 32px;
            margin-bottom: 15px;
            color: #5b4b45;
        }

        .introduccion p {
            font-size: 18px;
            line-height: 1.8;
        }

        .galeria {
            display: grid;
            grid-template-columns: repeat(
                auto-fit,
                minmax(280px, 1fr)
            );

            gap: 25px;
        }

        .foto {
            background: white;
            padding: 12px;
            border-radius: 16px;

            box-shadow:
                0 8px 25px rgba(0,0,0,0.12);

            transition: transform 0.3s ease;
        }

        .foto:hover {
            transform: translateY(-5px);
        }

        .foto img {
            width: 100%;
            height: 450px;
            object-fit: cover;
            border-radius: 10px;
            display: block;
        }

        .foto p {
            text-align: center;
            font-size: 17px;
            margin: 15px 5px 8px;
            color: #665b55;
        }

        .recuerdos {
            background: white;
            margin-top: 55px;
            padding: 35px;
            border-radius: 18px;

            box-shadow:
                0 8px 25px rgba(0,0,0,0.08);
        }

        .recuerdos h2 {
            text-align: center;
            color: #5b4b45;
            font-size: 30px;
            margin-top: 0;
        }

        .recuerdos > p {
            text-align: center;
            color: #756b65;
            font-size: 17px;
        }

        form {
            max-width: 700px;
            margin: 30px auto;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        input,
        textarea {
            width: 100%;
            padding: 14px;

            border: 1px solid #d6cec7;
            border-radius: 10px;

            font-family: inherit;
            font-size: 16px;

            margin-bottom: 18px;

            background: #faf8f5;
        }

        textarea {
            min-height: 140px;
            resize: vertical;
        }

        input:focus,
        textarea:focus {
            outline: none;
            border-color: #8c7468;
            box-shadow: 0 0 0 3px rgba(140,116,104,0.15);
        }

        button {
            width: 100%;
            padding: 15px;

            border: none;
            border-radius: 10px;

            background: #6f5a50;
            color: white;

            font-family: inherit;
            font-size: 17px;
            font-weight: bold;

            cursor: pointer;
        }

        button:hover {
            background: #57463e;
        }

        .lista-comentarios {
            max-width: 800px;
            margin: 40px auto 0;
        }

        .comentario {
            background: #f7f3ee;
            border-left: 4px solid #8c7468;

            padding: 18px;
            margin-bottom: 15px;

            border-radius: 8px;
        }

        .comentario strong {
            color: #5b4b45;
            font-size: 18px;
        }

        .comentario p {
            line-height: 1.6;
            margin-bottom: 0;
        }

        .sin-comentarios {
            text-align: center;
            color: #887c74;
            font-style: italic;
        }

        footer {
            text-align: center;
            margin-top: 60px;
            padding: 30px 20px;

            background: #463b36;
            color: #eee;
        }

        footer p {
            margin: 5px;
        }

        @media (max-width: 600px) {

            header {
                padding: 45px 15px;
            }

            header h1 {
                font-size: 38px;
            }

            header p {
                font-size: 17px;
            }

            .contenedor {
                width: 94%;
            }

            .foto img {
                height: auto;
                max-height: 550px;
            }

            .recuerdos {
                padding: 22px;
            }

            .introduccion h2 {
                font-size: 27px;
            }
        }

    </style>
</head>

<body>

<header>

    <h1>Remembrace</h1>

    <p>
        Un espacio para recordar, compartir y conservar momentos.
    </p>

</header>


<main class="contenedor">

    <section class="introduccion">

        <h2>Recuerdos que permanecen</h2>

        <p>
            Hay momentos que merecen ser conservados.
            Fotografías, historias y palabras que nos permiten
            mantener vivos aquellos recuerdos importantes.
        </p>

        <p>
            Este espacio fue creado para compartir fotografías
            y dejar un mensaje para el futuro.
        </p>

    </section>


    <section class="galeria">

        <div class="foto">

            <img
                src="{{ url_for('static', filename='fotos/foto1.jpg') }}"
                alt="Fotografía de recuerdo"
            >

            <p>
                Un momento para recordar.
            </p>

        </div>


        <div class="foto">

            <img
                src="{{ url_for('static', filename='fotos/foto2.jpg') }}"
                alt="Fotografía de recuerdo"
            >

            <p>
                Los recuerdos permanecen.
            </p>

        </div>

    </section>


    <section class="recuerdos">

        <h2>Deja un recuerdo</h2>

        <p>
            Escribe un mensaje, una historia o unas palabras
            que quieras conservar.
        </p>


        <form method="POST" action="{{ url_for('comentar') }}">

            <label for="nombre">
                Tu nombre
            </label>

            <input
                type="text"
                id="nombre"
                name="nombre"
                maxlength="50"
                required
                placeholder="Escribe tu nombre"
            >


            <label for="mensaje">
                Tu mensaje
            </label>

            <textarea
                id="mensaje"
                name="mensaje"
                maxlength="500"
                required
                placeholder="Escribe aquí tu recuerdo..."
            ></textarea>


            <button type="submit">
                Guardar recuerdo
            </button>

        </form>


        <div class="lista-comentarios">

            <h2>Mensajes</h2>

            {% if comentarios %}

                {% for comentario in comentarios %}

                    <div class="comentario">

                        <strong>
                            {{ comentario.nombre }}
                        </strong>

                        <p>
                            {{ comentario.mensaje }}
                        </p>

                    </div>

                {% endfor %}

            {% else %}

                <p class="sin-comentarios">
                    Todavía no hay mensajes.
                    Sé la primera persona en dejar uno.
                </p>

            {% endif %}

        </div>

    </section>

</main>


<footer>

    <p>Remembrace</p>

    <p>
        Un lugar para conservar los recuerdos.
    </p>

</footer>

</body>
</html>
"""


@app.route("/", methods=["GET"])
def inicio():

    return render_template_string(
        HTML,
        comentarios=comentarios
    )


@app.route("/comentar", methods=["POST"])
def comentar():

    nombre = request.form.get("nombre", "").strip()
    mensaje = request.form.get("mensaje", "").strip()

    # Validación del nombre
    if not nombre or len(nombre) < 2 or len(nombre) > 50:
        return "Nombre inválido", 400

    # Validación del mensaje
    if not mensaje or len(mensaje) < 2 or len(mensaje) > 500:
        return "Mensaje inválido", 400

    # Guardar comentario
    comentarios.append({
        "nombre": nombre,
        "mensaje": mensaje
    })

    return redirect(url_for("inicio"))


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
