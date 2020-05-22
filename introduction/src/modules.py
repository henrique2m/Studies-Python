import math
import random
import emoji
# from math import sqrt, floor

number = int(input('Digite um número: '))
square = math.sqrt(number)

print('-------Biblioteca Math---------')
print('A raiz de {} é igual a {}'.format(number, square))

print('-------Biblioteca Random---------')
print(random.random())
print(random.randint(1, 100))


# print('-------Biblioteca Emoji---------')
# print(emoji.emojize('Hello World :earth_americas:', use_aliases=True))

print('----------Desafios----------')
# - Desafios 

# 1 - crie um programa que leia um número real qualquer e mostre a parte inteira

numberReal = float(input('Informe um número real: '))
print('{:.0f}'.format(numberReal // 1))

# 2 - crie um programa que informe o valor da hipotenusa de um triângulo retaângulo

a = float(input('Cateto adjacente: '))
b = float(input('Cateto oposto: '))

h = ((a**2) + (b**2))**(1/2)
h2 = math.hypot(a, b)

print ('Hipotenusa (na mão) {:.2f} \n Hipotenusa {:.2f} (Biblioteca Math com método Hypot)'.format(h, h2))

# 3 - crie um program informe a partir de um ângulo informe seno, cosseno e a tangente de um triângulo

angle = float(input('Informe um ângulo: '))
sin = math.sin(angle)
cos = math.cos(angle)
tan = math.tan(angle)

print ('seno {:.2f}, cosseno {:.2f}, tangente {:.2f}'.format(sin, cos, tan))

# 4 - crie um programa para sortear um aluno e mostre uma lista com a ordem de sorteio dos demais alunos

numberStudents = int(input('Quantos alunos irão participar do sorteio? '))

students = []

for student in range(numberStudents):
    name = input('Informe o nome do estudante {}:'.format(student+1))
    students.append(name)
    
order = []
length = len(students)

print(length)

for new  in range(length):
    key = random.randint(0, length-1)
    order.append(students[key])
    students.pop(key)
    length = len(students)

print('O aluno que irá apagar o quadro hoje será o: {}'.format(order[0]))

print (order)

