import pymongo
import random
import time

# Parâmetros de conexão
uri_conexao = "mongodb://localhost:27017/"
nome_banco = "catalogo_livros"

contador = 1

try:
    # Registrar o tempo de início
    inicio = time.time()

    # Conectar ao MongoDB
    cliente_mongo = pymongo.MongoClient(uri_conexao)
    # Selecionar o banco de dados e a coleção
    db_mongo = cliente_mongo[nome_banco]
    # Selecionar a coleção
    colecao_livros = db_mongo["livros"]

    # Abre o arquivo CSV em modo de leitura
    with open('livros.csv', 'r', newline='', encoding='utf-8') as arquivo:
        # Leia a primeira linha
        linha = arquivo.readline()
        # Continue lendo linha por linha até que não haja mais linhas
        while linha:
            partes = linha.split(';')
            if len(partes) == 5:
                titulo = partes[0].replace("'", "")
                autor = partes[1]
                isbn = partes[2]
                paginas = partes[3]
                ano = partes[4]
                valor = round(random.uniform(40, 100), 2)

                livro = {
                    "titulo": titulo,
                    "autor": autor,
                    "isbn": isbn,
                    "paginas": int(paginas),
                    "ano": int(ano.replace('\n', '')),
                    "valor": valor
                }
                
                # Inserir o documento na coleção
                resultado = colecao_livros.insert_one(livro)
                print(titulo)

            # Leia a próxima linha
            linha = arquivo.readline()

    # Registrar o tempo de término
    fim = time.time()
    # Calcular o tempo decorrido
    tempo_decorrido = fim - inicio
    print("Tempo decorrido:", tempo_decorrido, "segundos")

except Exception as e:
    print("Ocorreu um erro:", e)
