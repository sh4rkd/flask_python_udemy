from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo!"

@app.route("/lele", methods=['POST', 'GET'])
def lele():
    #abort(401)
    #return redirect(url_for('show_post', post_id=1))
    # print(request.form)
    # print(request.form['llave1'])
    # print(request.form['llave2'])
    return render_template('lele.html')

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