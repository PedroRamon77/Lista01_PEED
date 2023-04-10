
lista = input("Digite a frase: ").split()

maiorPalavra = ""

for palavra in lista:
 if len(palavra) > len(maiorPalavra):
  maiorPalavra = palavra

print("A maior palavra da frase é: ",maiorPalavra)