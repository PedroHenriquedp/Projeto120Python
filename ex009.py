#Faça um um conversor de real para dolar, valor das moedas(29/03/2022) = $4,76, 0,039円 e €5,29
real = float(input ('Quanto dinheiro você tem na sua carteira ai? R$ '))
dolar = real/4.76
en = real/0.039
euro = real/5.29
print('Com {:.2f} reais, você pode comprar ${:.2f} dólares, {:.2f}円 ien, e  €{:.2f} euros'.format(real,dolar,en,euro))