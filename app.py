from flask import Flask, render_template # type: ignore

app = Flask(__name__, static_url_path='/static', template_folder='templates')


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/HOME")
def return_home():
    return render_template("index.html")

@app.route("/Características")
def caracteristicas():
    return render_template("caracteristicas.html")

@app.route("/Criação de Mapas")
def criacao_mapa():
    return render_template("map_avatar_creation.html")

@app.route("/Mapas Interessantes")
def mapas_interessantes():
    return render_template("interesting_maps.html")


@app.route("/Sobre Mim")
def about_me():
    return render_template("about-me.html")