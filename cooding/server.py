from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    print(f"⚠️ Datos simulados (NO REALES): Usuario: {username}, Contraseña: {password}")
    return "Error de autenticación (simulación)", 401

if __name__ == "__main__":
    app.run(port=5000, debug=True)