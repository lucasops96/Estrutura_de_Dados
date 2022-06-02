class Aluno:
    def __init__(self,nome,endereco):
        self.nome = nome
        self.endereco = endereco


class Curso:
    def __init__(self,nome,turno):
        self.nome = nome
        self.turno = turno
        self.alunos = []
        self.next = None


class Multilista:
    def __init__(self):
        self.head = None

    def cadastrarCurso(self,nome,turno):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = Curso(nome,turno)
        else:
            self.head = Curso(nome,turno)

    def buscarCurso(self,nome,turno):
        aux = self.head
        while aux and (aux.nome != nome or aux.turno != turno):
            aux = aux.next
        return aux
    
    def cadastrarAluno(self,nome,endereco,curso_nome,curso_turno):
        curso = self.buscarCurso(curso_nome,curso_turno)
        if curso:
            curso.alunos.append(Aluno(nome,endereco))
        else:
            print('Curso Inexistente')
        
    def relatorio(self):
        aux = self.head
        while aux:
            print(aux.nome,'-',aux.turno,'\n--------------------')
            for aluno in aux.alunos:
                print(aluno.nome)
                print('   ',aluno.endereco)
            
            aux = aux.next
            print()
    
    def total_alunos(self):
        aux = self.head
        total = 0
        while aux:
            total+= len(aux.alunos)
            aux = aux.next
        return total 


uepb = Multilista()
uepb.cadastrarCurso('Computação','manhã')
uepb.cadastrarCurso('Computação','noite')
uepb.cadastrarCurso('ADM','manhã')
uepb.cadastrarCurso('ADM','noite')
uepb.cadastrarAluno('Adrier','Jardim do Seridó','Computação','manhã')
uepb.cadastrarAluno('Wellington','Santa Luzia','Computação','manhã')
uepb.cadastrarAluno('Gambiarra Jr','Junco','Computação','noite')
uepb.cadastrarAluno('Maria','Crato','ADM','noite')
uepb.cadastrarAluno('Vitoria','Patos','ADM','manhã')
print('__________________')
uepb.relatorio()
print(uepb.total_alunos())
print('__________________')