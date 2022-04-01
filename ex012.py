#Faça um algoritmo que leia o salário de um funcionário e mostre seu
#novo salário, com 15% de aumento.
salario = float(input('Qual é o salário do Funcionário? R$'))
salarioAumento = salario+(salario*0.15)
print('O funcionário que ganhava R${:.2f}, com 15% de aumento passará a ganhar R${:.2f}'.format(salario,salarioAumento))
