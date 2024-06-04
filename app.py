from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__, static_url_path='/static', template_folder='templates')

# Configurações do MySQL
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '2#J5E8@s*8$WgokH'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'Contatos'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

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

@app.route("/Contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Obter dados do formulário
    nome_completo = request.form['nome_completo']
    email = request.form['email']
    telefone = request.form['telefone']
    comentario = request.form['comentario']

    # Conectar ao banco de dados
    conn = mysql.connection
    cursor = conn.cursor()

    # Inserir dados no banco de dados
    query = "INSERT INTO informacoes (nome_completo, email, telefone, comentario) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nome_completo, email, telefone, comentario))
    conn.commit()

    # Fechar a conexão com o banco de dados
    cursor.close()

    return render_template("contatos.html")


@app.route("/Consulta")
def consultar():
    conn = mysql.connection
    cursor = conn.cursor()
    query = "SELECT * FROM informacoes"
    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()
    return render_template("consulta.html", resultados=resultados)



if __name__ == '__main__':
    app.run(debug=True)
