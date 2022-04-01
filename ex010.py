#Faça um progroma que leia a largura e a altura de uma parede em metros, calcule
#a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
#de tinta, pinta uma área de 2m²

largura = float(input('Insira a largura em metros da parede '))
altura = float(input('Insira a altura em metros da parede '))
area = largura*altura
tinta = area/2
print('Sua parede tem dimensão de {}m x {}m e sua área é de {:.4f}m².\n'
    'Para pintar essa parede, você precisará de {:.4f}L de tinta.'.format(largura,altura,area,tinta))

