#Tarefa 001
print('---------Tarefa 001---------')
print('Hello world')

#Tarefa 002
print('---------Tarefa 002---------')
name = input("Digite o seu nome: ")
print('É um prazer te conhecer, {}!'.format(name))

#Tarefa 003
print('---------Tarefa 003---------')
a = input('Digite algo: ')
print("Só tem espaço? {}".format(a.isspace()))
print("É um número? {}".format(a.isnumeric()))
print("É alfabético? {}".format(a.isalpha()))
print("É alfanumérico? {}".format(a.isalnum()))
print("Está em maiúsculas? {}".format(a.isupper()))
print("Está em minúsculas? {}".format(a.islower()))
print("Está capitalizado? {}".format(a.istitle()))

print('---------Desafios---------')

# Desafios 

# 1 - crie um algoritmo mostre um número seu antecessor e sucessor
x = int(input('Digite um número inteiro: '))
print('{} Está entre {} e {}'.format(x, x-1, x+1))

# 2 - crie um algoritmo que leia uma número e mostre o seu dobro, triplo e a raiz quadrada

a = int(input('informe um número inteiro: '))
double = a*2
triple = a*3
square = a**(1/2)

print('O dobro de {} é: {}'.format(a, double))
print('O triplo de {} é: {}'.format(a, triple))
print('A raiz quadra de a {} é: {}'.format(a, square))

# 3 - crie uma algoritmo que leia dois números é mostre a média

n1 = float(input('Informe a sua primeira nota: '))
n2 = float(input('Informe a sua segunda nota: '))

m = (n1+n2)/2

print("Sua média foi: {}".format(m))

# 4 - crie um programa que leia um número inteiro e mostre sua tabuada

n3 = int(input('Informe um número inteiro: '))

for x in range(11):
    print('{} vezes {} é igual a {} \n'.format(n3, x, x*n3))

# 5 - crie um algoritmo que mostre que converta real para Dólar 

real = float(input('Quanto você tem na carteira? '))

converter = real/5.58 # valor do dólar em 21/05/2020

print('Com R$ {} reais você consegue comprar US$ {} dólares.'.format(real, converter))

# 6 - crie um algoritmo que calcule á area de uma parede e informe a quantidade de tinta necessária para pintá-la

width = float(input('Qual a largura da parede (em metros)?'))
height = float(input('Qual a altura da parede (em metros)?'))
area = width*height
ink = (area)/2.0 # litro de tinta por metro quadrado

print('A parede possui uma área de {} m², serão necessários {} L de tinta para pintá-la.'.format(area, ink))

# 7 - crie um algoritmo que calcule um desconto de 10% no valor de um produto

product = float(input('Informe o valor do produto: '))
discount = (product*5)/100

print('Com um desconto de 5 por cento o produto passará a valer R$ {}'.format(product-discount))

# 8 - crie um algoritmo que calcule um aumento de 10% no salário

salary = float(input('Informe seu salário: '))
add = (salary*15)/100

print('Com um aumento de 15 por cento seu sálario passará a ser ${}'.format(salary+add))
