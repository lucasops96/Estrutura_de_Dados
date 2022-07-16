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
        elif obj.nome < self.data.nome:
            if self.left:
                self.left.insert(obj)
            else:
                self.left = Uni(obj)
        elif obj.nome > self.data.nome:
            if self.right:
                self.right.insert(obj)
            else:
                self.right = Uni(obj)


    def imprimir_pre(self):
        if self.data:
            if self.left:
                self.left.imprimir_pre()
            print(self.left.data.nome if self.left else 'x','-',self.data.nome,'-',self.right.data.nome if self.right else 'x')
            if self.right:
                self.right.imprimir_pre()
    
    def buscarAluno(self,nome,matricula):
        if self.data.nome == nome and self.data.matricula == matricula:
            return self.data
        elif nome < self.data.nome:
            if self.left:
                aluno = self.left.buscarAluno(nome, matricula)
        elif nome > self.data.nome:
            if self.right:
                aluno = self.right.buscarAluno(nome, matricula)
        return aluno

    
    def cadastrarDisciplina(self,nome,matricula,disciplina):
        aluno = self.buscarAluno(nome, matricula)
        if aluno:
            aluno.disciplinas.append(Disciplina(disciplina))
            print('Disciplina adicionada')
        else:
            print('Aluno inexistente')

    def buscarDisciplina(self,nome,matricula,nome_da_disciplina):
        aluno = self.buscarAluno(nome, matricula)
        if aluno:
            for disciplina in aluno.disciplinas:
                if disciplina.nome == nome_da_disciplina:
                    return disciplina
    
    def cadastrarNota(self,nome,matricula,nome_da_disciplina,nota):
        disciplina = self.buscarDisciplina(nome, matricula, nome_da_disciplina)
        if disciplina:
            op = int(input('1 - Para Primeira nota I\n2 - Para Segunda nota II\n-->:'))
            if op == 1:
                disciplina.notas[0] = nota
                print('Primeira Nota adicionada I')
            else:
                disciplina.notas[1] = nota
                print('Segunda Nota adicionada II')
    
    def notasDeUmAluno(self,nome,matricula):
        aluno = self.buscarAluno(nome, matricula)
        if aluno:
            print('Nome: ',aluno.nome,' - Matrícula: ',aluno.matricula)
            print('Disciplinas:')
            for disciplina in aluno.disciplinas:
                print('        ',disciplina.nome,' Nota I:',disciplina.notas[0],' Nota II:',disciplina.notas[1])
    
    def menor(self,node):
        
        while node.left:
            node = node.left
        return node.data

    def remover(self,nome,node='root'):
        
        if nome < self.data.nome:
            self.left = self.left.remover(nome,self.left)
        elif nome > self.data.nome:
            self.right = self.right.remover(nome,self.right)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                aux = self.menor(self.right)
                self.data = aux
                self.right = self.right.remover(aux.nome,self.right)
        return self

    def removerDisciplina(self,nome,matricula,nome_da_disciplina):
        aluno = self.buscarAluno(nome, matricula)
        if aluno:
            i = 0
            for disciplina in aluno.disciplinas:
                if disciplina.nome == nome_da_disciplina:
                    aluno.disciplinas.pop(i)
                    print(nome_da_disciplina,' REMOVIDA')
                i+=1
    
    def removerNota(self,nome,matricula,nome_da_disciplina):
        disciplina = self.buscarDisciplina(nome, matricula, nome_da_disciplina)
        if disciplina:
            op = int(input('1 - Para Primeira nota I\n2 - Para Segunda nota II\n-->:'))
            if op == 1:
                disciplina.notas[0] = 0
                print('Primeira Nota REMOVIDA I')
            else:
                disciplina.notas[1] = 0
                print('Segunda Nota REMOVIDA II')




root = Uni()
root.insert(Aluno('miguel',2011))
root.insert(Aluno('sara',2009))
root.insert(Aluno('leticia',2002))
root.insert(Aluno('ana',2015))
root.insert(Aluno('marcos',2012))
root.insert(Aluno('paulo',2022))
root.imprimir_pre()


op = int(input('Digite 1 para iniciar o sistema: '))
while op != 0:
    op = int(input('1 - Para cadastrar Aluno\n2 - Cadastrar disciplina em Aluno\n3 - Cadastrar nota em disciplina de Aluno\n4 - Vizualizar Notas de um Aluno\n5 - Remover Aluno\n6 - Visualizar os nomes dos alunos em ordem alfabética\n7 - Remover Disciplina\n8 - Remover Nota de Disciplina\n-->:'))
    if op == 1:
        print('-------Cadastrar Aluno--------')
        nome = input('Digite o nome do Aluno: ')
        matricula = int(input('Digite a matricula do Aluno: '))
        root.insert(Aluno(nome,matricula))
        print('----------------------')
    elif op == 2:
        print('-------Cadastrar Disciplina--------')
        bnome = input('Digite o nome do Aluno: ')
        bmatricula = int(input('Digite a matricula do Aluno: '))
        disciplina = input('Digite o nome da Disciplina: ')
        root.cadastrarDisciplina(bnome,bmatricula,disciplina)
        print('----------------------')
    elif op == 3:
        print('-------Cadastrar Nota--------')
        cnome = input('Digite o nome do Aluno: ')
        cmatricula = int(input('Digite a matricula do Aluno: '))
        nome_da_disciplina = input('Digite o nome da Disciplina: ')
        nota = float(input('Digite a nota: '))
        root.cadastrarNota(cnome, cmatricula, nome_da_disciplina, nota)
        print('----------------------')
    elif op == 4:
        print('-------Vizualizar Nota--------')
        dnome = input('Digite o nome do Aluno: ')
        dmatricula = int(input('Digite a matricula do Aluno: '))
        root.notasDeUmAluno(dnome, dmatricula)
        print('----------------------')
    elif op == 5:
        print('-------Remover Aluno--------')
        rnome = input('Digite o nome do Aluno: ')
        root.remover(rnome)
        print('Aluno removido')
        print('----------------------')
    elif op == 6:
        print('-------Alunos em ordem--------')
        root.imprimir_pre()
        print('----------------------')
    elif op == 7:
        print('-------Remover Disciplina--------')
        enome = input('Digite o nome do Aluno: ')
        ematricula = int(input('Digite a matricula do Aluno: '))
        enome_da_disciplina = input('Digite o nome da Disciplina: ')
        root.removerDisciplina(enome, ematricula, enome_da_disciplina)
        print('----------------------')
    elif op == 8:
        print('-------Remover Nota de Disciplina--------')
        fnome = input('Digite o nome do Aluno: ')
        fmatricula = int(input('Digite a matricula do Aluno: '))
        fnome_da_disciplina = input('Digite o nome da Disciplina: ')
        root.removerNota(fnome, fmatricula, fnome_da_disciplina)
        print('----------------------')



