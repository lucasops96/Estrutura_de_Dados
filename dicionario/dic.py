arquivo = open('dicionario\scorpions-stilllovingyou.txt','r')
letra = arquivo.read().lower()

lista = letra.split()

ocorrencias = {}


for palavra in lista:
  ocorrencias[palavra] = ocorrencias.get(palavra,0) + 1


#max_ocorrencias = None
#max_palavra = None

#for k,v in ocorrencias.items():
#  if max_ocorrencias == None or v > max_ocorrencias:
#    max_ocorrencias = v
#    max_palavra = k

#print('A palavra é:',max_palavra,'com ',max_ocorrencias,'ocorrências.')


lista_palavras = sorted([(v,k) for k,v in ocorrencias.items()],reverse=True)

for i in range(10):
  print(lista_palavras[i][1],'-',lista_palavras[i][0])