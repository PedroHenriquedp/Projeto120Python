#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Qual o preço do produto em real '))
print('O produto receberá 5% de desconto')
produtodesc = produto-(produto*0.05)
print('O produto que custa R${}, na promoção com desconto de 5% vai custar R${}'.format(produto,produtodesc))
