from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo!"

@app.route("/lala")
def lala():
    return "Lala"

@app.route("/lala/<nombre>")
def lala_nombre(nombre):
    return "Lala " + nombre

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"El id del post es: {post_id}"