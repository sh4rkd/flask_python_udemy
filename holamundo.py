from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)

import mysql.connector
midb = mysql.connector.connect(
    host="localhost",
    user="SharkD",
    passwd="250893",
    database="prueba"
)
cursor = midb.cursor(dictionary=True)


@app.route("/")
def index():
    return "Hola Mundo!"

@app.route("/lele", methods=['POST', 'GET'])
def lele():
    cursor.execute("SELECT * FROM Usuario")
    usuarios = cursor.fetchall()
    #abort(401)
    #return redirect(url_for('show_post', post_id=1))
    # print(request.form)
    # print(request.form['llave1'])
    # print(request.form['llave2'])
    #return render_template('lele.html')
    return render_template('lele.html', usuarios=usuarios)

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

@app.route("/home", methods= ["GET"])
def home():
    return render_template("home.html", mensaje="Hola Mundo")

@app.route("/create", methods= ["GET", "POST"])
def create():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        edad = request.form["edad"]
        sql = "INSERT INTO Usuario (username, email, edad) VALUES (%s, %s, %s)"
        val = (username, email, edad)
        cursor.execute(sql, val)
        midb.commit()
        return redirect(url_for("lele"))
    else:
        return render_template("create.html")