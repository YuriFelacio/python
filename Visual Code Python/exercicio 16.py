temp = input("Digite FH se quiser passar de Fahrenheit para Celsius ou CS se quiser passar de Celsius para Fahrenheit: ")
num = float(input("Digite a temperatura: "))

if temp == ("FH"):
    conversao = (num - 32) * 5/9
    print("A conversão finalizou em: ",conversao,"°C")
elif temp ==("CS"):
    conversao =(num * 9/5) + 32
    print("A conversão finalizou em: ",conversao,"°F")

