from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)
    

# Criar a primeira pagina = primeira rota
@app.route("/")
def homepage():
    return render_template("index.html")

#roda nosso aplicativo
socketio.run(app, host="localhost")