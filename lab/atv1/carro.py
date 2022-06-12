def preco(k,d):
  p = (d * 60) + (k * 0.15)
  return p

km = float (input('Quantidade de km:'))
dias = int (input ('Quantidade de dias:'))

valor = preco(km,dias)
print('Valor do aluguel é:',valor)
