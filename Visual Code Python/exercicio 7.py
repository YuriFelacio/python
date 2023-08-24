#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
#de aumento.

a = float(input("Digite o preço de um produto: "))
desconto = a * 0.05
precodesconto = a - desconto
aumento = a * 0.15
precoaumento = a + aumento
print("O novo preço com o desconto é:",precodesconto,"e o novo preço com aumento é:",precoaumento,)