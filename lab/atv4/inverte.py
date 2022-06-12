class Stack:
    def __init__(self):
        self.head =[]
    
    def push(self,value):
        self.head.append(value)
    
    def pop(self):
        return self.head.pop()

    def isEmpty(self):
        return len(self.head) == 0


pilha = Stack()
palavra = input('Digite a palavra :')
t=len(palavra)
for i in palavra:
    pilha.push(i)
palavra = pilha.pop()
for i in range(t-1):
    palavra += pilha.pop()

print(palavra)