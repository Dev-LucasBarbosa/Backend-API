cd backend
python -m venv env
env/Scripts/activate
(env)pip install -r requirements.txt
(env)python main.py

http://localhost:8000/


cd frontend
npm install
npm run start
ir para http://localhost:3000

docker compose up -d

# default
engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")

# psycopg2
engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/mydatabase")

# pg8000
engine = create_engine("postgresql+pg8000://scott:tiger@localhost/mydatabase")
More notes on connecting to PostgreSQL at PostgreSQL.

MySQL
The MySQL dialect uses mysqlclient as the default DBAPI. There are other MySQL DBAPIs available, including PyMySQL:

# default
engine = create_engine("mysql://scott:tiger@localhost/foo")

# mysqlclient (a maintained fork of MySQL-Python)
engine = create_engine("mysql+mysqldb://scott:tiger@localhost/foo")

# PyMySQL
engine = create_engine("mysql+pymysql://scott:tiger@localhost/foo")


# sql server
engine = create_engine("mssql+pymssql://scott:tiger@hostname:port/dbname")

# FastAPI

## Começar iniciando o Docker
1. Configuramos o usuário e a senha no arquivo ```docker-compose.yml```;
1. Usar o ```docker ps``` no cmd do VSCode para ver se o docker está rodando corretamente na máquina;
1. Na pasta em que tiver o arquivo ```docker-compose.yml``` rodar também no cmd do VSCode o seguinte comando ```docker compose up -d``` para ligar o banco de dados na propria máquina.

## Configurando o Banco de Dados no Dbeaver 
1. Assim que abrir o Dbeaver criar uma conexão de DB usando o SGBD PostgreeSQL;
1. Configurar o host para ```localhost```;
1. Usuário e senha serão os mesmos do arquivo ```docker-compose.yml```;
1. Clicar em ```testar a conexão``` e assim que abrir a nova aba clicar em ```download```;
1. Após todas as operações acima pode clicar em ```concluir``` assim finalizando a criação da conexão do BD .

## Rodar a parte Backend 
1. Iremos entrar novamente no cmd do VSCode com o comando ```Ctrl + J``` no teclado;
1. ```cd backend``` para direcionarmos o caminho para a pasta backend;
1. ```python -m venv env``` para criar o ambiente
1. ```env\Scripts\activate``` esse comaando serve para ativar os scripts no ambiente criado;
1. ```(env) pip install -r requirements.txt``` 
