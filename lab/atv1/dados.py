def adiciona(l,c):
  if c < 4:
    v= int(input('Digite o dado:'))
    l.append(v)
    adiciona(l,c+1)


c=0
l=[1,2,3]
adiciona(l,c)
print(l)
