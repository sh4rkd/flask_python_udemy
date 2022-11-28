from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo!"

@app.route("/lele", methods=['POST'])
def lele():
    print(request.form)
    print(request.form['llave1'])
    print(request.form['llave2'])
    return "Lala"

@app.route("/lala/<nombre>")
def lala_nombre(nombre):
    return "Lala " + nombre

#GET, POST, PUT, PATCH, DELETE
@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def show_post(post_id):
    if request.method == 'POST':
        return f"POST {post_id}"
    else:
        return f"GET {post_id}" 