class Cliente:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.next = None
    
class Fila_prioridades:
    def __init__(self):
        self.ini = None
        self.fim = None
    
    def inserir_cliente(self,nome,idade):
        cliente = Cliente(nome, idade)
        if cliente.idade >= 65:
            if self.ini:
                aux = self.ini
                while aux.idade >= 65:
                    ant = aux
                    aux = aux.next
                cliente.next = ant.next
                ant.next = cliente
            else:
                self.ini = cliente
                cliente.next= self.fim
        else:
            if self.fim:
                aux = self.fim
                while aux.next:
                    aux = aux.next
                aux.next = cliente
            else:
                self.fim = cliente

    def print_clientes(self):
        aux = self.ini
        while aux:
            print(aux.nome,'-',aux.idade)
            aux = aux.next

c=Fila_prioridades()
c.inserir_cliente('Arthu',24)
c.inserir_cliente('Miguel',34)
c.inserir_cliente('Regina',76)
c.inserir_cliente('João',80)
c.inserir_cliente('Martha',25)
c.inserir_cliente('Luka',77)
c.inserir_cliente('Jose',80)
c.print_clientes()
