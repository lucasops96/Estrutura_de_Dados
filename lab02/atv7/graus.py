class TreeNode:
    def __init__(self,value=None):
        self.data = value
        self.left = self.right = None

    def insert(self,value):
        if not self.data:
            self.data = value
        elif value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = TreeNode(value)
        elif value > self.data:
            if self.right:
                self.right.insert(value)
            else:
                self.right = TreeNode(value)
    
    def graus(self):
        if self.data:            
            if self.left and self.right:
                print(self.data,'Grau->',2)
            elif self.left or self.right:
                print(self.data,'Grau->',1)
            else:
                print(self.data,'Grau->',0)
            if self.left:
                self.left.graus()
            if self.right:
                self.right.graus()
    
    def folhas(self):
        if not self.data:
            return 0
        elif not self.left and not self.right:
            return 1
        else:
            if self.left:
                e = self.left.folhas()
            else:
                e = 0
            if self.right:
                d = self.right.folhas()
            else:
                d = 0
            return e + d 
    
    def paiefilho(self):
        if self.data:
            if self.left:
                if self.left.left or self.left.right:
                    print(self.left.data)
                self.left.paiefilho()
            if self.right:    
                if self.right.right or self.right.left:
                    print(self.right.data)
                self.right.paiefilho()

root = TreeNode()
root.insert(10)
root.insert(7)
root.insert(9)
root.insert(5)
root.insert(20)
root.insert(25)
root.insert(13)
root.insert(2)

#print('Graus:')
#root.graus()
#print('Folhas:',root.folhas())
print('Pai e filho:')
root.paiefilho()
