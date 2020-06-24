# Uma string em Python é tradada com um Array

# Alguns métodos de manipulação de string

phrase = 'Curso em Vídeo Python'

print (phrase[1:5])
print (phrase[1:15:2])
print (phrase[:8])
print (phrase[4:])

print("Texto Longo")

#Crie um programa que leia o nome completo de uma pessoa e mostre:
    # O nome com todas as letras maiúsculas
    # O nome com todas as letras minúsculas
    # Quantas letras ao todo (sem considerar espaços)
    # Quantas letras tem o primeiro nome
name = str(input('Digite seu nome completo: '))

print(name.upper()) # Converte a string para maiúsculo
print(name.lower()) # Converte a string para minúsculo

length = len(name)
space = name.count(' ')

firstName = name.split(' ')
lengthFirstName = len(firstName[0])

print('A string possui {} caracteres sendo {} espaços.'.format(length, space))
print('O primeiro nome possui {} letras.'.format(lengthFirstName))

#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

number = input('Informe um número inteiro de 0 a 9999: ')

numberLength = len(number)

for index in range(numberLength):
    print("O digito {} é {}".format(index+1, number[index]))

#Crie um programa que leia o nome de uma cidade e diga se ela começa com a palavra "SANTO"

city = input('Informe uma cidade: ')
firstNameCity = city.split(' ')

print (firstNameCity[0].find('SANTO')) # Procura a incidência de uma string dentro de uma string 

if firstNameCity[0].upper() == 'SANTO' :
    print('A cidade começa com SANTO')
else:
    print('A palavra SANTO não foi encontrado.')


#Faça um programa que leia uma frase pelo teclado de mostre:
    #Quantas vezes aparece a letra "A"
    #Em que posições ela aparece pela primeira vez
    #Em que posição ela aparece a última vez

#strip  -> remove os espaços no inicio e no fim
#split -> separa a sting em de acordo com um elemento informado po padrão o separa em espaços
#rfind -> encontra a incidência de um elemento de começado do pelo fim da string 

phrase = str(input('Digite uma frase: ')).upper()

incidenceA = phrase.count('A') # retorna a incidência do elemento

if incidenceA > 0 :
    # retorna o indice do elemento
  
    incidenceFirstPosition = phrase.index('A')
    # (reversed) inverte ordem da frase e retorna uma lista de caracteres
    # (join) transforma a lista em uma strind
    phraseReversed = ''.join(reversed(phrase)) 
    # retorna o tamanho da string 
    phraseLength = len(phraseReversed) 
     # retorna a posição da ultima incidência de A
    incidenceLastPosition = phraseLength - (phraseReversed.index('A') + 1)

    print('A frase possui {} caractere(s) A'.format(incidenceA))
    print('O primero está na posição {}'.format(incidenceFirstPosition+1))
    print('O ultimo está na posição {}'.format(incidenceLastPosition+1))
else:
    print('O caractere "A" não foi encontrado na frase.')




