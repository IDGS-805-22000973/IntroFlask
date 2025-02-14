from flask import Flask, render_template, request

import forms

#Mandar a llamar las paginas que tenemos
app=Flask(__name__)



#Ruta ejemplo formulario
@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    mat=''
    nom=''
    ape=''
    email=''

    alumno_clase=forms.UserForm(request.form)
    if request.method=="POST":
        mat=alumno_clase.matricula.data
        nom=alumno_clase.nombre.data
        ape=alumno_clase.apellido.data
        email=alumno_clase.email.data
        print('Nombre: {}'.format(nom))
    return render_template("alumnos.html", form=alumno_clase)



@app.route("/")
def index():
    titulo="IDGS805"
    lista=["Pedro", "Juan", "Mario"]
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/Hola")
def hola():
    return "<h1>Hola, Mundo</h1>"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}!"

@app.route("/numero<int:n>")
def numero(n):
    return f"El numero es : {n}!"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"El ususario es : {username}! con id: {id}!"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"La suma es: {n1,n2}!"

@app.route("/default/")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola, {tem}!"


@app.route("/form1")
def form1():
    return '''
    <form>
    <label for=nombre> nombre: </label>
    </form>
    '''

@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def func():
    resultados = ""
    if request.method == "POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))
        operacion = request.form.get("operacion")

        if operacion == "suma":
            resultados = f"La suma de {num1} + {num2} = {num1 + num2}"
        elif operacion == "resta":
            resultados = f"La resta de {num1} - {num2} = {num1 - num2}"
        elif operacion == "multiplicacion":
            resultados = f"La multiplicación de {num1} x {num2} = {num1 * num2}"
        elif operacion == "division":
            if num2 == 0:
                resultados = "No se puede dividir entre cero."
            else:
                resultados = f"La división de {num1} / {num2} = {num1 / num2}"
    
    return render_template("OperasBas.html", resultado=resultados)


@app.route("/Cinepolis")
def cinepolis():
    return render_template("Cinepolis.html")


@app.route("/procesar_compra", methods=["POST"])
def fun():
    nombre = request.form.get("nombre")
    num_compradores = int(request.form.get("numCompradores", 0))
    num_boletos = int(request.form.get("numBoletos", 0))
    metodo_pago = request.form.get("metodoPago")

    if not nombre or num_compradores <= 0 or num_boletos <= 0 or not metodo_pago:
        return render_template("Cinepolis.html", procesar_compra="Datos incompletos o invalidos.")

    # boletos maximos por compradores
    max_boletos = num_compradores * 7
    if num_boletos > max_boletos:
        return render_template("Cinepolis.html", procesar_compra=f"No puedes comprar mas de {max_boletos} boletos")

    # calculo del precio
    precio = num_boletos * 12
    if num_boletos > 5:
        precio *= 0.85
    elif num_boletos > 2:
        precio *= 0.90
    if metodo_pago == "si":
        precio *= 0.90

    return render_template("Cinepolis.html", procesar_compra=f"Total a pagar: ${precio:.2f}")

if __name__ == "__main__":
    app.run(debug=True, port=3000)