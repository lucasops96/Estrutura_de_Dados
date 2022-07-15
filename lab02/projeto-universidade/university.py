class Disciplina:
    def __init__(self,nome):
        self.nome = nome
        self.notas = [0] * 2
class Aluno:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        self.disciplinas = []

class Uni:
    def __init__(self,obj=None):
        self.data = obj
        self.left = self.right = None
    
    def insert(self,obj):
        if not self.data:
            self.data = obj
        elif obj.matricula < self.data.matricula:
            if self.left:
                self.left.insert(obj)
            else:
                self.left = Uni(obj)
        elif obj.matricula > self.data.matricula:
            if self.right:
                self.right.insert(obj)
            else:
                self.right = Uni(obj)


    def imprimir_pre(self):
            if self.data:
                print(self.left.data.nome if self.left else 'x','<-',self.data.nome,'->',self.right.data.nome if self.right else 'x')
                if self.left:
                    self.left.imprimir_pre()
                if self.right:
                    self.right.imprimir_pre()

root = Uni()
root.insert(Aluno('miguel',2011))
root.insert(Aluno('sara',2009))
root.insert(Aluno('leticia',2002))
root.insert(Aluno('suely',2015))
root.insert(Aluno('marcos',2012))
root.imprimir_pre()
        
        
