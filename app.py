from flask import Flask, render_template, request, redirect
from data import fetch_dersler, insert_ders, fetch_ogrenciler

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", name="Ahmet")


@app.route("/iletisim")
def contact():
    return render_template("contact.html", name="Ahmet")


@app.route("/hakkimizda")
def about():
    return render_template("about.html", name="Ahmet")


@app.route("/dersler")
def course():
    dersler = fetch_dersler()
    return render_template("course.html", dersler=dersler)


@app.route("/ders-ekle")
def course_create():
    return render_template("course_create.html")


@app.route("/ders-ekle-post", methods=['POST'])
def course_create_post():
    kod = request.form.get('kod')  # Access a specific field
    baslik = request.form.get('baslik')  # Access a specific field
    insert_ders(baslik, kod)
    return redirect("/dersler")


@app.route("/ogrenciler")
def student():
    ogrenciler = fetch_ogrenciler()
    return render_template("student.html", ogrenciler=ogrenciler)
