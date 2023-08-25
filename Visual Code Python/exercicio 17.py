""" Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde h corresponde à altura):
• Homens: (72.7 x h) - 58
• Mulheres: (62, 1 x h) - 44, 7 """

altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo(H/F): ")

if (sexo == "H"):
    conta = (72.7 * altura) - 58
    print("Seu peso ideal é: ",conta)
elif(sexo == "F"):
    conta = (62.1 * altura) - 44.7
    print("Seu peso ideal é: ",conta)