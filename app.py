from flask import Flask, render_template, request, redirect, session, abort
from data import fetch_dersler, insert_ders, fetch_ogrenciler
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {
    'ahmet': {'password': 'ahmet', 'role': 'admin'},
    'samet': {'password': 'samet', 'role': 'manager'},
    'yuzlu': {'password': 'yuzlu', 'role': 'student'},
    'azra': {'password': 'azra', 'role': 'student'}
}


@app.context_processor
def inject_session():
    return {'session': session}


@app.errorhandler(403)
def forbidden(e):
    return render_template("error-403.html")


def roles_required(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'username' not in session or session.get('role') not in roles:
                abort(403)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/iletisim")
def contact():
    return render_template("contact.html")


@app.route("/hakkimizda")
def about():
    return render_template("about.html")


@app.route("/dersler")
@roles_required('admin', 'student', 'manager')
def course():
    dersler = fetch_dersler()
    return render_template("course.html", dersler=dersler)


@app.route("/ders-ekle")
@roles_required('admin', 'manager')
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


@app.route("/kayit-ol")
def signup():
    return render_template("signup.html")


def signup_post():
    kod = request.form.get('kod')  # Access a specific field
    baslik = request.form.get('baslik')  # Access a specific field
    insert_ders(baslik, kod)
    return redirect("/")


@app.route("/giris-yap")
def signin():
    return render_template("signin.html")


@app.route("/giris-yap-post", methods=['POST'])
def signin_post():
    username = request.form['username']
    password = request.form['password']
    user = users.get(username)
    if user and user['password'] == password:
        session['username'] = username
        session['role'] = user['role']
    return redirect("/")


@app.route('/cikis-yap')
def logout():
    session.clear()
    return redirect("/")
