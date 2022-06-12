class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0
    
    def append(self,value):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = Node(value)
        else:
            self.head = Node(value)
        self.__size += 1
    
    def __len__(self):
        return self.__size
    
    def __getitem__(self,index):
        if self.head:
            aux = self.head
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError('Indice fora da lista')
            return aux.data
        else:
            raise IndexError('Lista vazia')
    
    def __setitem__(self,index,value):
        if self.head:
            aux = self.head
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError('Indice fora da lista')
            aux.data = value
        else:
            raise IndexError('Lista vazia')
    
    def __str__(self):
        output='['
        aux = self.head
        while aux:
            output += str(aux.data)
            if aux.next:
                output+=', '
            aux = aux.next
        output +=']'
        return output

    def remover_first(self):
        if self.head:
            if self.head.next:
                aux = self.head
                self.head = self.head.next
                del aux
            else:
                del self.head
                self.head = None
        else:
            raise IndexError('Lista Vazia')

    def remover_last(self):
        if self.head:
            aux = self.head
            ant = None
            while aux.next:
                ant = aux
                aux = aux.next
            if ant == None:
                del aux
                self.head = None
            else:
                ant.next = None
                del aux
        else:
            raise IndexError('Lista Vazia')
    
    def pares(self):
        if self.head:
            aux = self.head
            while aux:
                if aux.data % 2 == 0:
                    print(aux.data)
                aux = aux.next
        else:
            raise IndexError('Lista Vazia')
    
l=LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.append(7)
l.append(8)
l.append(9)
l.append(10)

print(l)
l.remover_first()
print(l)
l.remover_last()
print(l)
l.pares()
