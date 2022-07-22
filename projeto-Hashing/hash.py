class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

class Hash:
    def __init__(self):
        self.tabela = []
        for i in range(10):
            self.tabela.append([])
    
    def insert(self,funcionario):
        firstLetter = ord(funcionario.nome[0])
        position = firstLetter % 10
        self.tabela[position].append(funcionario)

    def buscarSalario(self,nome_do_funcionario):
        firstLetter = ord(nome_do_funcionario[0])
        position = firstLetter % 10
        for funcionario in self.tabela[position]:
            if funcionario.nome == nome_do_funcionario:
                return funcionario.salario
    
    def printFuncionarios(self):
        for i in self.tabela:
            for j in i:
                print(j.nome,' - ',j.salario,end=' ')


tabelaFuncionarios = Hash()
op = int(input('1 - Para iniciar o programa: '))
while op != 0:
    op = int(input('\n1 - Inserir funcionário\n2 - Buscar salário de um funcionário\n0 - exit\n-->:'))
    if op == 1:
        print('-------------Inserir funcionário-------------')
        nome = input('Digite nome do funcionário: ')
        salario = float(input('Digite o salário do funcionário: '))
        tabelaFuncionarios.insert(Funcionario(nome,salario))
        print('Funcionário Adicionado')
        print('---------------------------------------------')
    elif op == 2:
        print('------Buscar salário de um funcionário-------')
        nome_do_funcionario = input('Digite nome do funcionário: ')
        buscar_salario = tabelaFuncionarios.buscarSalario(nome_do_funcionario)
        print('R$ ',buscar_salario)
        print('---------------------------------------------')
    else:
        print('exit ...')
