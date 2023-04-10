
lista = input("Digite os números da lista: ").split()

numPar = []

for i in lista:
 if int(i) % 2 == 0 and int(i) != 0:
  numPar.append(i)

if numPar:
 print("Os números pares são: ")
 for i in numPar:
  print("",i)

