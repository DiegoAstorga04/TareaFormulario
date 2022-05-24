from flask import Flask, render_template, request
import datetime
app = Flask(__name__)

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/info", methods=["get","post"])
def datos():
    name = request.form.get("nombre")
    lname = request.form.get("apellidos")
    mail = request.form.get("mail")
    number = request.form.get("numero")
    date = request.form.get("fecha")
    ndate = datetime.datetime.strptime(date,"%Y-%m-%d")
    return render_template("ingresado.html", name=name, lname=lname, mail=mail, number= number, ndate=str(ndate))
