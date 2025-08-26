#Que receba em uma variável o nome de uma escola e o nome do aluno. Ao final
#deve mostrar no console conforme a baixo:
nome = input("Digite seu nome:")
escola = input("Digite sua escola:")
print("Meu nome é", nome, "e estudo em", escola)

#Que receba o nome e a idade de 2 pessoas. Ao final ele deve escreve conforme a
#baixo:
nome1 = input ("Digite seu nome:")
idade1 = int(input("Digite sua idade:"))
nome2 = input("Digite outro nome:")
idade2 = int(input("Digite a outra idade:"))
print("Nome da primeira pessoa", nome1, "idade da primeira pessoa", idade1 )
print("Nome da segunda pessoa", nome2, "idade da segunda pessoa",idade2)

#Que receba 2 números e mostre o resultado das quatro operações: soma, subtração, divisão e multiplicação.
a = int(input("Digite um número:"))
b = int(input("Digite outro número:"))
soma=a+b
sub=a-b
multi=a*b
divisao=a//b
print("Adição:", soma)
print("Subtração:", sub)
print("Multiplicação:", multi)
print("Divisão:", divisao)

#Que solicite o lado de um quadrado e calcule a sua área.
lado = int(input("Digite o lado:"))
multi = lado*lado
print("A área do quadrado é",multi)

#Que receba um número e calcule o cubo deste número
lado = int(input("Digite o lado:"))
multi = lado*3
print("A área do quadrado é",multi)

#Que receba do teclado 4 notas e escreva a média aritmética dessas notas.
a = float(input("Digite a nota 1:"))
b = float(input("Digite a nota 2:"))
c = float(input("Digite a nota 3:"))
d = float(input("Digite a nota 4:"))
media = a+b+c+d
total= media//4
print("A média aritmética é:", total)

#Construa um algoritmo de uma loja de peças em que ele realize o que se pede abaixo: a)Receba código de uma peça b)Receba valor unitário da peça. c)Receba quantidade de peças vendidas. )Calcule o valor total da peça (quantidade x valor unitário da peça).
#e)Mostre o código da peça e seu valor total.
peca = int(input("codigo da peça: "))
valor = float(input("digite o valor da peça: "))
venda = int(input("Quantas peças foram vendidas: "))
vdporpc = venda*valor
print("a peça de codigo: ",peca)
print("vendeu o total de: ",vdporpc)