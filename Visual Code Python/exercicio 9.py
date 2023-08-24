#Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
#mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
#Euros.

input("Digite seu nome: ")
rs = float(input("Digite quantos reais você tem: "))
dol = rs * 0.21
eu = rs * 0.19

print("Você teria",dol,"dolares e",eu,"euros")