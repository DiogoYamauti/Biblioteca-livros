## Funcionalidades

- Listagem de livros como autor, título, ISBN, páginas etc...
- Páginação com controles de navegação para:
  - Ir para a primeira página.
  - Ir para a página anterior.
  - Navegar entre cinco páginas consecutivas.
  - Ir para a próxima página.
  - Ir para a última página.
- Contador que exibe a quantidade de livros na página atual e total de livros no catálogo.

## Pré-requisitos

Ter o Node.js, MongoDB e o Python instalados na máquina.

- Node.js
- MongoDB
- Python

## Instruções para Instalação e Execução

1. Clonar o repositório:
git clone https://github.com/seu-usuario/nome-do-repositorio.git

2. Navegue até o diretório do projeto:
cd nome-do-repositorio

3. Instalar dependências:
npm install

4. Instalar pymongo no MongoDB:
pip install pymongo

5. O MongoDB deve estar rodando localmente em **mongodb://localhost:27017** e que há uma base de dados chamada **biblioteca** com uma coleção **livros**.

6. Insira os livros no banco:
py inserir_livros.py

7. Inicie o servidor:
node app.js

8. Abra o navegador e acessesando **http://localhost:3000** para ver a aplicação.

## Estrutura do Projeto

- **app.js**: Possui a configuração do servidor e a lógica.
- **public/css/styles.css**: Estilos CSS.
- **inserir_livros.py**: Script Python para inserir dados no MongoDB a partir de um arquivo CSV.
- **livros.csv**: Arquivo CSV contendo os dados dos livros.
- **package.json**: Dependências.
- **views/index.ejs**: Template EJS.