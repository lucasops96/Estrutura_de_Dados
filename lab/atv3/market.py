produtos = {}

def cadastrar():
    produto = input('Digite o nome do Produto :')
    valor = float(input('Digite o valor :'))
    if produto in produtos:
        return 'Produto já se encontra em estoque'
    produtos[produto] = valor
    return 'Produto cadastrado'

def pesquisar():
    produto = input('Nome do produto :')
    valor = produtos.get(produto,0)
    if valor == 0:
        return 'Produto não cadastrado'
    return produto+' R$:'+str(valor)

def remover():
    produto = input('Nome do produto :')
    if produto in produtos:
        valor = produtos.pop(produto)
        return produto+' R$:'+str(valor)+' REMOVIDO!!!'
    else:
        return 'Produto não está cadastrado'

def imprimir():
    for k,v in produtos.items():
        print(k,'-R$',v)

op=0
while op != 5:
    op = int(input('1-Cadastrar Produtos\n2-Pesquisar\n3-Remover\n4-Lista\n5-Sair\n:'))
    if op == 1:
        print(cadastrar())
    elif op == 2:
        print(pesquisar())
    elif op == 3:
        print(remover())
    elif op == 4:
        imprimir()
    else:
        print('Saindo ...')