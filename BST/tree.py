class BSTnode:
    def __init__(self,value=None):
        self.data =  value
        self.left = self.right = None
    
    def insert(self,value):
        if not self.data:
            self.data = value
        elif value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTnode(value)
        elif value > self.data:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTnode(value)
    
    def imprimir_pre(self):
        if self.data:
            print(self.left.data if self.left else 'x','<-',self.data,'->',self.right.data if self.right else 'x')
            if self.left:
                self.left.imprimir_pre()
            if self.right:
                self.right.imprimir_pre()
    
    def imprimir_central(self):
        if self.data:
            if self.left:
                self.left.imprimir_central()
            print(self.data,end=' ')
            if self.right:
                self.right.imprimir_central()
    
    def imprimir_pos(self):
        if self.data:
            if self.left:
                self.left.imprimir_pos()
            if self.right:
                self.right.imprimir_pos()
            print(self.data,end=' ')
    
    # def tamanho(self):
    #     if not self.data:
    #         return 0
    #     else:
    #         if self.left:
    #             esq = self.left.tamanho()
    #         else:
    #             esq = 0
    #         if self.right:
    #             dire = self.right.tamanho()
    #         else:
    #             dire = 0
    #         return esq + dire + 1


    def tamanho(self):
        if not self.data:
            return 0
        else:
            return (self.left.tamanho() if self.left else 0) + (self.right.tamanho() if self.right else 0) + 1 
    
    def soma(self):
        if not self.data:
            return 0
        else:
            return (self.left.soma() if self.left else 0) + (self.right.soma() if self.right else 0) + self.data
    
    def altura(self):
        if not self.data:
            return -1
        else:
            alt_e = self.left.altura() if self.left else -1
            alt_d = self.right.altura() if self.right else -1

            return alt_e + 1 if alt_e > alt_d else alt_d + 1

    def balanceada(self):
        if not self.data:
            return True
        else:
            x = self.left.balanceada() if self.left else True
            y = self.right.balanceada() if self.right else True
            a = self.left.altura() if self.left else -1
            b = self.right.altura() if self.right else -1
            z = abs(a-b) <=1
            return  x and y and z
    
    def gerar_lista(self,lista):
        if self.data:
            if self.left:
                self.left.gerar_lista(lista)
            lista.append(self.data)
            if self.right:
                self.right.gerar_lista(lista)
    
    def destruir(self):
        if self.data:
            if self.left:
                self.left.destruir()
            if self.right:
                self.right.destruir()
            del self.data
            del self
    
    def gerar_arvore(self,lista,ini,fim):
        meio = (ini + fim) // 2
        self.data = lista[meio]
        if ini <= meio - 1:
            self.left = BSTnode()
            self.left.gerar_arvore(lista, ini, meio-1)
        else:
            self.left = None
        if meio+1 <= fim:
            self.right=BSTnode()
            self.right.gerar_arvore(lista, meio+1, fim)
        else:
            self.right = None
    
    def balanceamento_estatico(self):
        if not self.balanceada():
            l=[]
            self.gerar_lista(l)
            self.destruir()
            self.gerar_arvore(l,0, len(l)-1)
            return self

    def espelho(self):
        if self.left:
            self.left.espelho()
        if self.right:
            self.right.espelho()
        if self.left or self.right:
            aux = self.left
            self.left = self.right
            self.right = aux



root = BSTnode()
root.insert(5)
root.insert(2)
root.insert(8)
root.insert(3)
root.insert(7)
root.insert(9)
# root.insert(13)
# root.insert(2)
# root.insert(1)
# print('Pré-ordem:', end=' ')
# root.imprimir_pre()
# print('\nOrdem central: ', end=' ')
# root.imprimir_central()
# print('\nPós-ordem: ', end=' ')
# root.imprimir_pos()
# print('\nTamanho: ',root.tamanho())
# print('Soma: ',root.soma())
# print('Altura: ',root.altura())
# print('Balanceada: ',root.balanceada())
# root = root.balanceamento_estatico()
# print('-----------------')
# print('Altura: ',root.altura())
# print('Balanceada: ',root.balanceada())
root.imprimir_pre()
root.espelho()
print('-----------------')
root.imprimir_pre()

