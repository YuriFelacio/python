#Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
#trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
#ao final mostrar seu nome e salário final calculado.

nome = input("Digite seu nome: ")
nhoras = float(input("Digite o seu numero de horas trabalhadas: "))
vhoras = float(input("Digite o valor da hora trabalhada: "))

sal = nhoras*vhoras
inss = sal - (sal * 0.02)

print("Seu nome é:",nome,"E seu salário final é:",inss)