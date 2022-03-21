#Instrução: Faça o dobro, triplo e a raiz quadrada de um número inserido.
import math
ban = int(input('Digite um valor inteiro: '))
print('O seu número é {} o dobro desse número é {} e o triplo é {}'.format(ban,ban*2,ban*3))
raiz = math.sqrt(ban)
print('A raiz quadrada de {} é exatamente: {}'.format(ban,raiz))