from configuracoes import *
from modelos import Personagem

@app.route("/")
def index():
    return 'Sistema de cadastro de personagens. ' + '<a href="/listar_personagens">Operação Listar</a>'

@app.route("/listar_personagens")
def listar_personagens():
    requisicao = requests.get('http://127.0.0.1:5000/listar_personagens')
    personagens_em_json = requisicao.json()
    personagens_em_python = []
    for persona in personagens_em_json:
        pe = Personagem(**persona)
        personagens_em_python.append(pe)
    return render_template('listar_personagens.html', listagem=personagens_em_python)
    

app.run(debug=True, port=4999)