""" Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
a. Soma de 2 numeros.
b. Diferença entre 2 números (maior pelo menor).
c.Produto entre 2 números.
d. Divisão entre 2 números (o denominador não pode ser zero). """

while True:
    op=input("Escolha entre as opções:\n"
          "Para soma entre 2 numeros digite soma.\n"
          "Para diferença entre 2 numeros digite subtração.\n"
          "Para produto entre 2 numeros digite produto.\n"
          "Para divisão entre 2 numeros digite divisão.\n"
          "Para encerrar as opcoes digite encerrar.\n"
          ":")
    
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    if (op == "soma"):
        print("a soma dos dois numeros resultou em:",num1 + num2)
    elif (op == "subtração"):
        print("a subtração entre os numeros resultou em:",num1 - num2)
    elif (op == "produto"):
        print("O produto entre os dois numeros resultou em:",num1 * num2)
    elif (op == "divisão"):
        if((num1 == 0) or (num2 == 0)):
            print("Impossivel dividir por 0.")
            break
        print("A divisão entre os dois numeros resultou em :",num1 / num2)
    elif (op == "encerrar"):
        break
    
