#Um professor quer sortear um dos seus quatro alunos
#para apagar o quadro. Faça um programa que ajude ele, lendo
#o nome deles e escrevendo o nome do escolhido

import random
aluno1 = str(input('Nome do aluno 1 '))
aluno2 = str(input('Nome do aluno 2 '))
aluno3 = str(input('Nome do aluno 3 '))
aluno4 = str(input('Nome do aluno 4 '))
aluno5 = str(input('Nome do aluno 5 '))
lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
escolhido = random.choice(lista)
print('O escolhido foi {}'.format(escolhido))
