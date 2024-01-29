import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários,
    onde cada dicionário representa um produto.
    
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    ...
    #Criando uma lista de categorias Vazia, para inserir todos os elementos
    lista_categorias = []
    #Percorrendo toda a lista que foi passada por parâmetro 
    for i in dados:
        #Verificando se a categoria não está na lista
        if i['categoria'] not in lista_categorias: 
            #Se ela não tiver na lista, então a categoria é adicionada a lista de categorias
            lista_categorias.append(i['categoria'])
    
    #Retornando a lista de categorias
    return lista_categorias


def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    ...
    #Criando uma lista vazia para armazenar cada produto da categoria
    categorias = []
    #Percorrendo todos os dados da lista
    for cat in dados:
        #Verificando se a categoria do produto é igual a categoria passada por parâmetro
        if cat['categoria'] == categoria:
            #Se for da categoria passada, o produto é inserido na lista
            categorias.append(cat)

    #Retorna a Lista de todos os produtos daquela categoria    
    return categorias


def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    ...
    #Criando um objeto vazio, para armazenar o maior preco
    objeto = None
    #Percorrendo todos os dados da lista
    for cat in dados:
        #Verificando se a categoria é a mesma que foi passada por parâmetro 
        if cat['categoria'] == categoria:
            #Verifica se o Objeto ainda está vazio | Isso serve para a primeira iteração, onde o objeto está vazio!
            #Ou Verifica se o valor do preço atual, é maior que o que foi passado anteriormente!
            #Tranforma a variável preço em Float para fazer a comparação
            if objeto is None or float(cat['preco']) > float(objeto['preco']):
                #Se sim, o objeto atual é armazenado na variável objeto
                objeto = cat

    #Retorna o objeto com maior valor da categoria    
    return objeto


def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    ...

    #Criando um objeto vazio, para armazenar o maior preco
    objeto = None
    #Percorrendo todos os dados da lista
    for cat in dados:
        #Verificando se a categoria é a mesma que foi passada por parâmetro 
        if cat['categoria'] == categoria:
            #Verifica se o Objeto ainda está vazio | Isso serve para a primeira iteração, onde o objeto está vazio!
            #Ou Verifica se o valor do preço atual, é menor que o que foi passado anteriormente!
            #Tranforma a variável preço em Float para fazer a comparação
            if objeto is None or (float(cat['preco']) < float(objeto['preco'])):
                #Se sim, o objeto atual é armazenado na variável objeto
                objeto = cat

    #Retorna o objeto com maior valor da categoria    
    return objeto


def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    ...
    #Ordenou a lista pelo preço e inseriu na lista dados_ordenados, Transformou o preço em float, para ser feito a ordenação
    dados_ordenados = sorted(dados, key=lambda produto: float(produto['preco']))
    #Reverteu a lista para pegar os maiores valores
    dados_ordenados.reverse()

    #Retornou a lista dos 10 maiores valores
    return dados_ordenados[:10]


def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    ...
    #Ordenou a lista pelo preço e inseriu na lista dados_ordenados, Transformou o preço em float, para ser feito a ordenação
    dados_ordenados = sorted(dados, key=lambda produto: float(produto['preco']))
   

    #Retornou a lista dos 10 menores valores
    return dados_ordenados[:10]

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    ...
    op = 1
    while op != 0:
        op = int(input("1. Listar categorias\n2. Listar produtos de uma categoria\n3. Produto mais caro por categoria\n4. Produto mais barato por categoria\n5. Top 10 produtos mais caros\n6. Top 10 produtos mais baratos\n0. Sair    \n\n"))
        
        if op == 1:
            #Listar por Categorias
            lista = listar_categorias(dados)
            print('\n\n-----LISTA DE CATEGORIAS----- \n\n')
            for categ in lista:
                print(f"CATEGORIA: {categ}")
            print('\n\n')

        elif op == 2:
            #Listar Produtos de uma Categoria
            #Mostrando as Categorias a serem escolhidas
            lista = listar_categorias(dados)
            for categ in lista:
                print(f"CATEGORIA: {categ}")
            #Pedindo ao usuário para informar a categoria que deseja listar
            categoria_busca = (input("Digite uma categoria: "))
            categorias = []
            #Buscando a categoria digitada e inserindo na variável categorias
            categorias = listar_por_categoria(dados, categoria_busca)
            #Listando os produtos da categoria buscada
            print(f'\n\n-----LISTA DE PRODUTOS DA CATEGORIA {categoria_busca}-----\n\n')
            for i in categorias:
                print(f"ID: {i['id']}")
                print(f"PREÇO: {i['preco']}")
                print(f"CATEGORIA: {i['categoria']}\n")

        elif op == 3:
            #Produto mais caro por categoria
            #Mostrando as Categorias a serem escolhidas
            lista = listar_categorias(dados)
            for categ in lista:
                print(f"CATEGORIA: {categ}")
            #Pedindo ao usuário para informar a categoria que deseja listar
            categoria_busca = (input("Digite uma categoria: "))
            produto = produto_mais_caro(dados, categoria_busca)
            print(f'\n\n-----PRODUTO MAIS CARO DA CATEGORIA {categoria_busca}-----\n\n')
            print(f"ID: {produto['id']}")
            print(f"PREÇO: {produto['preco']}")
            print(f"CATEGORIA: {produto['categoria']}\n")

        elif op == 4:
            #Produto mais Barato por categoria
            #Mostrando as Categorias a serem escolhidas
            lista = listar_categorias(dados)
            for categ in lista:
                print(f"CATEGORIA: {categ}\n")
            #Pedindo ao usuário para informar a categoria que deseja listar
            categoria_busca = (input("Digite uma categoria: "))
            produto = produto_mais_barato(dados, categoria_busca)
            print(f'\n\n-----PRODUTO MAIS BARATO DA CATEGORIA {categoria_busca}-----\n\n')
            print(f"ID: {produto['id']}")
            print(f"PREÇO: {produto['preco']}")
            print(f"CATEGORIA: {produto['categoria']}\n")
        elif op == 5:
            #Top 10 produtos mais caros
            top_10 = []
            top_10 = top_10_caros(dados)
            print(f'\n\n-----TOP 10 DE PRODUTOS MAIS CAROS-----\n\n')
            for i in top_10:
                print(f"ID: {i['id']}")
                print(f"PREÇO: {i['preco']}")
                print(f"CATEGORIA: {i['categoria']}\n")
                
        elif op == 6:
            #Top 10 produtos mais baratos
            top_10 = []
            top_10 = top_10_baratos(dados)
            print(f'\n\n-----TOP 10 DE PRODUTOS MAIS BARATOS-----\n\n')
            for i in top_10:
                print(f"ID: {i['id']}")
                print(f"PREÇO: {i['preco']}")
                print(f"CATEGORIA: {i['categoria']}\n")
                
        elif (op > 6) or (op < 0):
            print("Opção Inválida")


# Programa Principal - não modificar!
d = obter_dados()
menu(d)
print('\n\n-----PROGRAMA FINALIZADO-----\n\n')