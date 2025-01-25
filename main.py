from flask import Flask

app=Flask(__name__)
#Mandar a llamar las paginas que tenemos

@app.route("/")
def index():
    return "Hello, World , hola"


@app.route("/Hola")
def hola():
    return "Hola, Mundo"


if __name__ == "__main__":
    app.run(debug=True, port=3000)