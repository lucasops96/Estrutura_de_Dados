class Disciplina:
    def __init__(self,nome):
        self.nome = nome
        self.notas = [0] * 2
    
    def calcularMedia(self):
        self.media = (self.notas[0] + self.notas[1]) / 2
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


    def imprimirAlunos(self):
        if self.data:
            if self.left:
                self.left.imprimirAlunos()
            print('-',self.data.nome,'-',self.data.matricula)
            if self.right:
                self.right.imprimirAlunos()
    
    def buscarAluno(self,nome,matricula,aluno=None):
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
            print('Algum dos dados está incorreto')

    def buscarDisciplina(self,nome,matricula,nome_da_disciplina):
        aluno = self.buscarAluno(nome, matricula)
        if aluno:
            for disciplina in aluno.disciplinas:
                if disciplina.nome == nome_da_disciplina:
                    return disciplina
        else:
            print('Algum dos dados está incorreto')
    
    def cadastrarNota(self,nome,matricula,nome_da_disciplina):
        disciplina = self.buscarDisciplina(nome, matricula, nome_da_disciplina)
        if disciplina:
            n1 = float(input(' - Digite Primeira nota I: '))
            n2 = float(input(' - Digite Segunda nota II: '))
            disciplina.notas[0] = n1
            disciplina.notas[1] = n2
            print('Notas adicionadas')
    
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
            op = int(input('1 - Para Remover Primeira nota I\n2 - Para Remover Segunda nota II\n-->:'))
            if op == 1:
                disciplina.notas[0] = 0
                print('Primeira Nota REMOVIDA I')
            else:
                disciplina.notas[1] = 0
                print('Segunda Nota REMOVIDA II')
    
    def atualizarAluno(self,nome,matricula):
        aluno = self.buscarAluno(nome, matricula)
        if aluno:
            aluno.nome = input('Atualize o nome do Aluno: ')
            aluno.matricula = int(input('Atualize a Matrícula: '))
            print('Aluno atualizado')
        else:
            print('Algum dos dados está incorreto')
    
    def atualizarDisciplina(self,nome,matricula,nome_da_disciplina):
        disciplina = self.buscarDisciplina(nome, matricula, nome_da_disciplina)
        if disciplina:
            disciplina.nome = input('Atualize o nome da Disciplina: ')
            disciplina.notas[0] = float(input('Atualize a Primeira Nota: '))
            disciplina.notas[1] = float(input('Atualize a Segunda Nota: '))
            print('Disciplina e Notas Atualizadas')
    
    def vizualizarMedia(self,nome,matricula,nome_da_disciplina):
        disciplina = self.buscarDisciplina(nome, matricula, nome_da_disciplina)
        if disciplina:
            disciplina.calcularMedia()
            print('Nome:',nome,' - ',matricula)
            print(disciplina.nome,' Nota I: ',disciplina.notas[0],' Nota II: ',disciplina.notas[1])
            print('Média: ',disciplina.media)
        else:
            print('Algum dos dados está incorreto')
    
    def vizualizarMediasMaior(self):
        if self.data:
            if self.left:
                self.left.vizualizarMediasMaior()
            for disciplina in self.data.disciplinas:
                disciplina.calcularMedia()
                if disciplina.media >= 7:
                    print(self.data.nome,' - ',disciplina.nome,' Média: ',disciplina.media)
            if self.right:
                self.right.vizualizarMediasMaior()
    
    def vizualizarMediasMenor(self):
        if self.data:
            if self.left:
                self.left.vizualizarMediasMenor()
            for disciplina in self.data.disciplinas:
                disciplina.calcularMedia()
                if disciplina.media < 7:
                    print(self.data.nome,' - ',disciplina.nome,' Média: ',disciplina.media)
            if self.right:
                self.right.vizualizarMediasMenor()




root = Uni()



op = int(input('Digite 1 para iniciar o sistema: '))
while op != 0:
    op = int(input('\n\n1 - Para cadastrar Aluno\n2 - Cadastrar disciplina em Aluno\n3 - Cadastrar nota em disciplina de Aluno\n4 - Vizualizar Notas de um Aluno\n5 - Remover Aluno\n6 - Visualizar os nomes dos alunos em ordem alfabética\n7 - Remover Disciplina\n8 - Remover Nota de Disciplina\n9 - Atualizar aluno\n10 - Atualizar disciplina de aluno\n11 - Visualizar a média do aluno em uma disciplina\n12 - Visualizar médias\n0 - Para Encerrar o sistema\n-->:'))
    if op == 1:
        print('-------Cadastrar Aluno--------')
        nome = input('Digite o nome do Aluno: ')
        matricula = int(input('Digite a matrícula do Aluno: '))
        root.insert(Aluno(nome,matricula))
        print('Aluno Cadastrado')
        print('----------------------')
    elif op == 2:
        print('-------Cadastrar Disciplina--------')
        bnome = input('Digite o nome do Aluno: ')
        bmatricula = int(input('Digite a matrícula do Aluno: '))
        disciplina = input('Digite o nome da Disciplina: ')
        root.cadastrarDisciplina(bnome,bmatricula,disciplina)
        print('----------------------')
    elif op == 3:
        print('-------Cadastrar Nota--------')
        cnome = input('Digite o nome do Aluno: ')
        cmatricula = int(input('Digite a matrícula do Aluno: '))
        nome_da_disciplina = input('Digite o nome da Disciplina: ')
        root.cadastrarNota(cnome, cmatricula, nome_da_disciplina)
        print('----------------------')
    elif op == 4:
        print('-------Vizualizar Nota--------')
        dnome = input('Digite o nome do Aluno: ')
        dmatricula = int(input('Digite a matrícula do Aluno: '))
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
        root.imprimirAlunos()
        print('----------------------')
    elif op == 7:
        print('-------Remover Disciplina--------')
        enome = input('Digite o nome do Aluno: ')
        ematricula = int(input('Digite a matrícula do Aluno: '))
        enome_da_disciplina = input('Digite o nome da Disciplina: ')
        root.removerDisciplina(enome, ematricula, enome_da_disciplina)
        print('----------------------')
    elif op == 8:
        print('-------Remover Nota de Disciplina--------')
        fnome = input('Digite o nome do Aluno: ')
        fmatricula = int(input('Digite a matrícula do Aluno: '))
        fnome_da_disciplina = input('Digite o nome da Disciplina: ')
        root.removerNota(fnome, fmatricula, fnome_da_disciplina)
        print('----------------------')
    elif op == 9:
        print('-------Atualizar aluno--------')
        anome = input('Digite o nome do Aluno: ')
        amatricula = int(input('Digite a matrícula do Aluno: '))
        root.atualizarAluno(anome, amatricula)
        print('----------------------')
    elif op == 10:
        print('--------Atualizar disciplina de aluno-------')
        aunome = input('Digite o nome do Aluno: ')
        aumatricula = int(input('Digite a matrícula do Aluno: '))
        aunome_da_disciplina = input('Digite o nome da Disciplina: ')
        root.atualizarDisciplina(aunome, aumatricula, aunome_da_disciplina)
        print('----------------------')
    elif op == 11:
        print('--------Visualizar a média do aluno-------')
        mnome = input('Digite o nome do Aluno: ')
        mmatricula = int(input('Digite a matrícula do Aluno: '))
        mnome_da_disciplina = input('Digite o nome da Disciplina: ')
        root.vizualizarMedia(mnome, mmatricula, mnome_da_disciplina)
        print('----------------------')
    elif op == 12:
        print('--------Visualizar as médias dos alunos-------')
        kind = int(input('1 - Para Médias Maior ou igual a 7\n2 - Para Médias Menor que 7\n-->:'))
        if kind == 1:
            root.vizualizarMediasMaior()
        else:
            root.vizualizarMediasMenor()
        print('----------------------')



