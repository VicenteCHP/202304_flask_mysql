
# Flask
from flask import Flask, render_template, request, redirect, url_for

# Models
from models.usuarios import Usuario


# Flask app
# ----------------------------------------------------------------------------
app = Flask(__name__)


@app.route("/usuarios")
def usuarios_list():

    usuarios = Usuario.get_all()
    return render_template("usuarios/list.html", usuarios=usuarios)


@app.route("/usuarios/<int:id>/detail")
def usuarios_detail(id):

    data = {"id": id}
    usuario = Usuario.get_one(data)
    return render_template("usuarios/detail.html", usuario=usuario)


@app.route("/usuarios/create", methods=["GET", "POST"])
def usuarios_create():


    if request.method == "POST":
        data = {
            "nombre": request.form["nombre"],
            "apellido": request.form["apellido"],
            "correo_electronico": request.form["correo_electronico"],
        }
        Usuario.create(data)
        return redirect(url_for("usuarios_list"))
    return render_template("usuarios/create.html")


@app.route("/usuarios/<int:id>/update", methods=["GET", "POST"])
def usuarios_update(id):

    data = {"id": id}
    usuario = Usuario.get_one(data)
    if request.method == "POST":
        data = {
            "id": id,
            "nombre": request.form["nombre"],
            "apellido": request.form["apellido"],
            "correo_electronico": request.form["correo_electronico"],
        }
        Usuario.update(data)
        return redirect(url_for("usuarios_list"))
    return render_template("usuarios/update.html", usuario=usuario)


@app.route("/usuarios/<int:id>/delete")
def usuarios_delete(id):

    data = {"id": id}
    Usuario.delete(data)
    return redirect(url_for("usuarios_list"))
    


# Programa principal
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=8000)
