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
                    raise IndexError('Índice fora da lista')
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
                    raise IndexError('Índice fora da lista')
            aux.data = value
        else:
            raise IndexError('Lista vazia')

    def __str__(self):
        output = '['
        aux = self.head
        while aux:
            output += str(aux.data)
            if aux.next:
                output+=', '
            aux = aux.next
        output +=']'
        return output

    def busca_binaria(self,x,inf=0,sup=None):
        if sup is None:
            sup = len(self)-1
        
        if inf <= sup:
            meio = (inf+sup)//2

            if x == self[meio]:
                return meio
            if x < self[meio]:
                return self.busca_binaria(x,inf,meio-1)
            else:
                return self.busca_binaria(x,meio+1,sup)
        return -1

    def ordenar(self,lista):
        i=0
        j=0
        lm = LinkedList()
        while i < len(self) and j < len(lista):
            if self[i] < lista[j]:
                lm.append(self[i])
                i+=1
            elif lista[j] < self[i]:
                lm.append(lista[j])
                j+=1
            else:
                lm.append(self[i])
                i+=1
                j+=1
        while i < len(self):
            lm.append(self[i])
            i+=1
        while j < len(lista):
            lm.append(lista[i])
            j+=1
        return lm

l = LinkedList()
l.append(1)
l.append(2)
l.append(5)
l.append(6)
l.append(9)
l.append(10)
l.append(11)
print(l)
lm = LinkedList()
lm.append(2)
lm.append(3)
lm.append(4)
lm.append(7)
lm.append(8)
print(lm)
#print(len(l))
#print(l[1])
#l[1]=46
#print(l[1])
#print(l)
#o = l.ordenar(lm)
#print(o)

print(l.busca_binaria(5))