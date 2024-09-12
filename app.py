# API - É um lugar para disponibilizar recursos e / ou funcionalidades
# 1. Objetivo - Criar um API que disponibiliza a criação, consulta, edição e exclusão de livros.
# 2. URL Base - Local para qual estaremos fazendo nossas requisições - localhost
# 3. Endpoints - Quais são os tipos de funcionalidades que eu vou disponibilizar no meu API
#   - localhost/livros (GET)
#   - localhost/livros (POST)
#   - localhost/livros/id (GET)
#   - localhost/livro/id (PUT)
#   - localhost/livros/id (DELETE)
# 4. Quais recursos vou disponibilizar - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Secrets of the Millionaire Mind',
        'autor': 'T. Harv Eker'
    },
    {
        'id': 2,
        'título': 'The Divine Matrix',
        'autor': 'Gregg Braden'
    },
        {
        'id': 3,
        'título': 'Outwitting the Devil',
        'autor': 'Napoleon Hill'
    }
]

# Consultar (Todos)
@app.route('/livros', methods = ['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar (id)
@app.route('/livros/<int:id>', methods = ['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar
@app.route('/livros/<int:id>', methods = ['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
@app.route('/livros', methods = ['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>', methods = ['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port = 5000, host = 'localhost', debug = True)