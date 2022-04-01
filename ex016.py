#Faça um programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comrpimento da hipotenusa.

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = co**2+ca**2
hipotenusaFinal = math.sqrt(hipotenusa)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusaFinal))
