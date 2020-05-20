print('------------------Saída de dados--------------------')

print('Hello World!') # Quebra de linha é equivalente ao ";", finalizando um comando;

print('-----------Operadores aritméticos---------------------')

print(1+2) # adição

print(2-1) # subtração

print(2*6) # multiplicação

print(6/2) # divisão

print(2**3) # exponenciação

print(4%2) # módulo 

print('--------------Operadores de concatenação------------')

print('Henrique '+ 'Moreira') # Concatena tipos de dados iguais

print('Henrique', 1.71, 60.00) # Concatena tipos de dados diferêntes 

print('-----------------Entrada de dados ------------------')

name = input('Qual é o seu nome jovem padawan?')

print(name, ' é um nome bonito! (:')


#Tipos primitivos
#int -> Números inteiros
#float -> Números reais 
#bool -> boolean 
#str -> string


# exercício 1
n1 = int(input('Informe um número. '))
n2 = int(input('Informe outro número. '))

print(n1+n2)

print('------------Tipo de dados--------------')

# exercício 2
n3 = input('Digite algo: ')
print(type(n3)) #Retorna o tipo de dados

# exercício 3
print('----------Método (format())---------')
n4 = int(input('Digite um número: '))
n5 = int(input('Digite outro número:'))
soma = (n4 + n5)
print('A soma de {} e {} é {}'.format(n4, n5, soma))

print('----------Método (isnumeric)---------')
# exercício 4
n6 = input('Informe um valor: ')
print(n6.isnumeric(), n6.isspace())


 