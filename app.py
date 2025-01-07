from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


usuarios = []  # Lista para armazenar usuários
catalogo = []  # Lista para armazenar livros
emprestimos = {}  # Dicionário para armazenar empréstimos (email: [livros])



@app.route("/")
def index():
    return render_template("index.html")



@app.route("/cadastrar_usuario", methods=["GET", "POST"])
def cadastrar_usuario():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]

        # Adiciona o usuário na lista de usuários
        usuarios.append({"nome": nome, "email": email})
        return redirect(url_for("index"))

    return render_template("cadastrar_usuario.html")


@app.route("/cadastrar_livro", methods=["GET", "POST"])
def cadastrar_livro():
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        ano = request.form["ano"]

        
        catalogo.append({"titulo": titulo, "autor": autor, "ano": ano, "disponivel": True})
        return redirect(url_for("index"))

    return render_template("cadastrar_livro.html")



@app.route("/listar_usuarios")
def listar_usuarios():
    return render_template("listar_usuarios.html", usuarios=usuarios)



@app.route("/listar_livros")
def listar_livros():
    return render_template("listar_livros.html", catalogo=catalogo)



@app.route("/emprestar_livro", methods=["GET", "POST"])
def emprestar_livro():
    if request.method == "POST":
        email = request.form["email"]
        titulo = request.form["titulo"]

        
        usuario = next((u for u in usuarios if u["email"] == email), None)
        livro = next((l for l in catalogo if l["titulo"] == titulo and l["disponivel"]), None)

        
        if not usuario:
            return render_template("emprestar_livro.html", error="Usuário não encontrado!", usuarios=usuarios, catalogo=catalogo)
        if not livro:
            return render_template("emprestar_livro.html", error="Livro não disponível ou não encontrado!", usuarios=usuarios, catalogo=catalogo)

       
        livro["disponivel"] = False
        emprestimos[email] = emprestimos.get(email, []) + [livro]
        return redirect(url_for("index"))

    return render_template("emprestar_livro.html", usuarios=usuarios, catalogo=catalogo, error=None)



@app.route("/listar_emprestimos")
def listar_emprestimos():
    return render_template("listar_emprestimos.html", emprestimos=emprestimos, usuarios=usuarios)



if __name__ == "__main__":
    app.run(debug=True)




   
