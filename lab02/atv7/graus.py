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
    
    def imprimir_pre(self):
        if self.data:
            print(self.left.data if self.left else 'x','<-',self.data,'->',self.right.data if self.right else 'x')
            if self.left:
                self.left.imprimir_pre()
            if self.right:
                self.right.imprimir_pre()
    
    

root = TreeNode()
root.insert(10)
root.insert(7)
root.insert(9)
root.insert(5)
root.insert(20)
root.insert(25)
root.insert(13)
root.insert(2)
print('Pré-ordem:')
root.imprimir_pre()
