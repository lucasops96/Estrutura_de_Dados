class Cliente:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.next = None
    
class Fila_prioridades:
    def __init__(self):
        self.ini = None
        self.fim = None

    def inserir_cliente(self, nome, idade):
        if not self.ini: # fila vazia
            self.ini = Cliente(nome,idade)
            self.fim = self.ini
        elif idade < 65: # cliente jovem
            self.fim.next = Cliente(nome,idade)
            self.fim = self.fim.next
        elif self.ini.idade < 65: # fila só com jovens
            aux = Cliente(nome,idade)
            aux.next = self.ini
            self.ini = aux
        elif self.fim.idade >= 65: # fila só com idosos
            self.fim.next = Cliente(nome,idade)
            self.fim = self.fim.next
        else: # fila mista
            aux = self.ini
            while aux.idade >= 65:
                ant = aux
                aux = aux.next
            novo = Cliente(nome,idade)
            ant.next = novo
            novo.next = aux
    

    def print_clientes(self):
        aux = self.ini
        while aux:
            print(aux.nome,'-',aux.idade)
            aux = aux.next


c=Fila_prioridades()
c.inserir_cliente('Carlos',24)
c.inserir_cliente('Emanuel',34)
c.inserir_cliente('Socorro',66)
c.inserir_cliente('Miguelito',90)
c.inserir_cliente('Bernadez',45)
c.inserir_cliente('Luka',87)
c.print_clientes()