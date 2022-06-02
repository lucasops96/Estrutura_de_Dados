class Stack:
    def __init__(self):
        self.head = []

    def push(self,value):
        self.head.append(value)
    
    def pop(self):
        return self.head.pop()

    def isEmpty(self):
        return len(self.head) == 0

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
                    raise IndexError('Indice fora da Lista')
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
                    raise IndexError('Indice fora da Lista')
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

    def _getNode(self,index):
        if self.head:
            aux = self.head
            for i in range(index):
                if aux.next:
                    aux = aux.next
                else:
                    raise IndexError('Indice fora da Lista')
            return aux
        else:
            raise IndexError('Lista vazia')

        
    def insert(self,index,value):
        node = Node(value)
        if index ==0:
            node.next = self.head
            self.head = node
        else:
            aux = self._getNode(index-1)
            node.next = aux.next
            aux.next = node
        self.__size +=1

    def extend(self,lista):
        aux = self.head
        while aux.next:
            aux = aux.next
        aux.next = lista.head
        

    def pop(self,index=-1):
        if index == -1:
            if not self.head:
                raise IndexError('lista vazia')
            elif not self.head.next:
                del self.head
                self.head=None
            else:
                aux = self.head
                while aux.next:
                    ant = aux
                    aux = aux.next
                del aux
                ant.next = None
        else:
            if self.__size <= index:
                raise IndexError('indice fora da lista')
            elif index == 0:
                aux = self.head
                self.head = aux.next
                del aux
            else:
                aux = self.head
                for i in range(index):
                    ant = aux
                    aux = aux.next
                ant.next = aux.next
                del aux

    def print_partial(self,ant,prox):
        aux = self.head
        for i in range(prox):
            if i > ant:
                print(aux.data)
            aux = aux.next

    def inverse(self):
        pilha = Stack()
        aux = self.head
        while aux:
            pilha.push(aux.data)
            aux = aux.next
        i = 0
        while i < len(self):
            self[i] = pilha.pop()
            i+=1
        
        

            


l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)

l.append(6)
l.append(7)
l.append(8)

l2 = LinkedList()
l2.append(90)
l2.append(80)
l2.append(77)
l2.append(60)
l2.append(50)

print(l)

l.pop(4)

print(l)

#print(len(l))
#print(l[4])
#l[4] = 77
#print(l[4])
#print(l)




#l.insert(0,10)
#l.insert(3,499)

#l.extend(l2)

#l.print_partial(2,4)

#l.inverse()