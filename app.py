from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "cecytej-30-aniversario"

@app.route("/")
def inicio():
    return render_template("index.html", title="Inicio")

@app.route("/historia")
def historia():
    return render_template("historia.html", title="Nuestra historia")

@app.route("/voces")
def voces():
    return render_template("voces.html", title="Voces que dejan huella")

@app.route("/orgullo")
def orgullo():
    return render_template("orgullo.html", title="Orgullo CECyTEJ")

@app.route("/eventos")
def eventos():
    return render_template("eventos.html", title="Celebremos juntos")

@app.route("/futuro", methods=["GET", "POST"])
def futuro():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        mensaje = request.form.get("mensaje", "").strip()
        if nombre and mensaje:
            flash("¡Gracias por compartir tu mensaje para el futuro del CECyTEJ!")
        else:
            flash("Completa tu nombre y tu mensaje para poder enviarlo.")
        return redirect(url_for("futuro"))
    return render_template("futuro.html", title="Nuestro futuro")

if __name__ == "__main__":
    app.run(debug=True)
