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



# Edita carro
@app.route(f'/carros/<int:id>', methods=['PUT'])
def update_carro(id):
    # conn = mydb.cursor()

    try:
        # Dados enviados pelo cliente
        dados = request.json
        marca = dados.get('marca')
        modelo = dados.get('modelo')
        ano = dados.get('ano')

        # Validação dos dados recebidos
        if not marca or not modelo or not ano:
            return jsonify({"error": "Todos os campos (marca, modelo, ano) são obrigatórios"}), 400

        # Construindo a consulta com parâmetros
        sql = """
                UPDATE carros 
                SET marca = %s, modelo = %s, ano = %s 
                WHERE id = %s
            """

        valores = (marca, modelo, ano, id)

        # Executando a consulta
        conn = mydb.cursor()
        conn.execute(sql, valores)
        mydb.commit()

        # Verificando se alguma linha foi atualizada
        if conn.rowcount == 0:
            return jsonify({"error": "Carro não encontrado"}), 404

        return jsonify({"message": "Carro atualizado com sucesso!"}), 200

    except Exception as e:
        print(f"Erro ao atualizar carro: {e}")
        return jsonify({"error": "Erro interno do servidor"}), 500


# Edita carro
@app.route(f'/carros/<int:id>', methods=['DELETE'])
def delete_carro(id):
    try:
        conn = mydb.cursor()

        # Corrigido o SQL para incluir a cláusula FROM
        sql = "DELETE FROM carros WHERE id = %s"
        valores = (id,)

        conn.execute(sql, valores)
        mydb.commit()

        if conn.rowcount == 0:
            return jsonify({"error": "Carro não encontrado"}), 404

        return jsonify({"message": "Carro deletado com sucesso!"}), 200

    except Exception as e:
        print(f"Erro ao deletar carro: {e}")
        return jsonify({"error": "Erro interno do servidor"}), 500



app.run()
