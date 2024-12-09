import mysql.connector
from flask import Flask, make_response, jsonify, request
from bd import Carros

mydb = mysql.connector.connect(
    host='localhost',
    user='MainUser',
    passwd='MainPassword',
    database='Pycoderbr'
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


# Lista carros
@app.route('/carros', methods=['GET'])
def get_carros():

    conn = mydb.cursor()
    conn.execute('SELECT * FROM carros')

    lista_carros = conn.fetchall()

    carros = list()
    for carro in lista_carros:
        carros.append(
            {
                'id': carro[0],
                'marca': carro[1],
                'modelo': carro[2],
                'ano': carro[3],
            }
        )


    return make_response(
        jsonify(
            message='Lista de carros',
            data=carros
        )
    )

# Adiciona carro na memoria da lista
@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json

    conn = mydb.cursor()

    sql = f"INSERT INTO carros (marca, modelo, ano) VALUES ('{carro['marca']}', '{carro['modelo']}', {carro['ano']})"

    conn.execute(sql)
    mydb.commit()


    return make_response(
        jsonify(
            message='Carro cadastrado',
            data=carro
        )
    )



app.run()
