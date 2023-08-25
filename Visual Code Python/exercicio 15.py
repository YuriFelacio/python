temp = float(input("Digite a temperatura atual: "))

if(temp < 14 ):
    print("A temperatura atual está fria. ")
elif((temp >= 14) and (temp <= 24)):
    print("A temperatura atual está agradável. ")
elif(temp > 25):
    print("A temperatura atual está quente. ")