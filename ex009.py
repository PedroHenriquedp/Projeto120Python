#Faça um um conversor de real para dolar, valor do dolar (29/03/2022) = 4,76
real = float(input ('Quanto dinheiro você tem na sua carteira ai? R$ '))
dolar = real/4.76
print('Com {:.2f} você pode comprar {:.2f}'.format(real,dolar))