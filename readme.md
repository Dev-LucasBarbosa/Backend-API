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
1. ```(env) pip install -r requirements.txt``` para baixarmos as bibliotecas certas que estão no arquivo ```requirements.txt```;
1.  Endpoint para ser usado é o ```uvicorn main:app --host 127.0.0.1 --port:8002```;
1. ```(env) python main.py``` para rodar o programa.
