#O mesmo professor do desafio anterior quer sortear a ordem de
#apresentação de trabalhos dos alunos. Faça um programa que leia
#o nome dos quatro alunos e mostre a ordem sorteada.

import random
aluno1 = str(input('Nome do aluno 1 '))
aluno2 = str(input('Nome do aluno 2 '))
aluno3 = str(input('Nome do aluno 3 '))
aluno4 = str(input('Nome do aluno 4 '))
aluno5 = str(input('Nome do aluno 5 '))
lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
random.shuffle(lista)
print('A ordem de apresentação será')
print(lista)

