# teste-Python


para vriar a venv execute "python -m venv venv" no diretorio raiz do projeto

para ativar eexecutar a venv do projeto execute no diretorio principal o comando ".\venv\Scripts\activate"

instalar o Flask dentro da venv com ela já ativa: pip install flask



Comando no terminal Windows para criar a imagem Docker do banco de dados

docker build -t pycoder-db .



Comando para iniciar a imagem gerada

docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=RootPassword -e MYSQL_DATABASE=Pycoderbr -e MYSQL_USER=MainUser -e MYSQL_PASSWORD=MainPassword pycoder-db



Instalar para conectar com o mysql

pip install mysql-connector-python
