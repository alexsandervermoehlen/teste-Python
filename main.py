from flask import Flask, make_response, jsonify, request

from bd import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Lista carros
@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
        jsonify(
            message='Lista de carros',
            data=Carros
        )
    )

# Adiciona carro na memoria da lista
@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            message='Carro cadastrado',
            data=carro
        )
    )



app.run()
