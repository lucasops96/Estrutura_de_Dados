class Livro:
    def __init__(self,nome):
        self.nome = nome

class Aluno:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros = []
        self.next = None
    
class Biblioteca:
    def __init__(self):
        self.head = None
    
    def cadastrarAluno(self,nome,matricula):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = Aluno(nome, matricula)
        else:
            self.head = Aluno(nome, matricula)
    
    def buscarAluno(self,nome,matricula):
        aux = self.head
        while aux and ( aux.nome != nome or aux.matricula != matricula):
            aux = aux.next
        return aux
    
    def casdastrarLivro(self,nome,matricula,livro):
        aluno = self.buscarAluno(nome, matricula)
        if aluno:
            aluno.livros.append(Livro(livro))
        else:
            print('Aluno Inexistente')
    
    def removerAluno(self,nome,matricula):
        if self.head:
            aux = self.head
            if aux.nome == nome and aux.matricula == matricula:
                self.head = aux.next
                del aux
            else:
                while aux and (aux.nome != nome or aux.matricula != matricula):
                    ant = aux
                    aux = aux.next
                ant.next = aux.next
                del aux
    
    def removerLivro(self,nome,matricula,livro):
        aluno = self.buscarAluno(nome, matricula)
        if aluno:
            i = 0
            for li in aluno.livros:
                if li.nome == livro:
                    posicao = i
                i+=1
            aluno.livros.pop(posicao)
        
    
    def relatorio(self):
        aux = self.head
        while aux:
            print(aux.nome,'-',aux.matricula)
            for livro in aux.livros:
                print('        ',livro.nome)
            aux = aux.next


b = Biblioteca()
b.cadastrarAluno('marcos',2345)
b.cadastrarAluno('leticia',2346)
b.cadastrarAluno('suely',2347)
b.cadastrarAluno('maria',2348)
b.casdastrarLivro('marcos',2345,'Pequeno Principe')
b.casdastrarLivro('marcos',2345,'Miguel Perdido no Alasca')
b.casdastrarLivro('leticia',2346,'Memorias de um Sargento de Milicias')
b.casdastrarLivro('suely',2347,'Menino do pijama listrado')
b.relatorio()
b.removerAluno('maria',2348)
b.removerLivro('marcos',2345,'Pequeno Principe')
b.relatorio()