#Escreva um programa que pergunta a quantidade em KM percorridos
#por um carro alugado e a quantidade de dias pelos quais
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
#custa R$60 por dia e R$0,15 por KM rodado.
diaria = int(input('Quantos dias o carro foi alugados? '))
gasolina = float(input('Quantos KM foram rodados? '))
gasolinaFinal = gasolina*0.15
precoFinal = gasolinaFinal+diaria*60
print('O total a pagar é de R${:.2f}'.format(precoFinal))

