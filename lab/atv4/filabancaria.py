class Fila:
    def __init__(self):
        self.head = []

    def push(self,value):
        self.head.append(value)
    
    def pop(self):
        return self.head.pop(0)

    def isEmpty(self):
        return len(self.head) == 0

    def imprimir(self):
        for i in range(len(self.head)):
            print(self.head[i])

class Pessoa:
    def __init__(self,nome,cpf,conta):
        self.nome = nome
        self.cpf = cpf
        self.conta = conta
    
    def __str__(self):
        return self.nome + ' CPF:'+str(self.cpf)+' Conta:'+ str(self.conta)+'\n'


clientes =Fila()
op = 0
while op!=4:
    op = int(input('1-Adicionar clientes\n2-Lista de clientes\n3-Remover cliente\n4-SAIR\n:'))
    if op == 1:
        nome = input('Digite o nome:')
        cpf = int(input('Digite CPF:'))
        conta = int(input('Digite conta:'))
        newcliente = Pessoa(nome,cpf,conta)
        clientes.push(newcliente)
    elif op == 2:
        clientes.imprimir()
    elif op == 3:
        clientes.pop()
    else:
        print('Saindo do programa ...')


