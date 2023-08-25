""" Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.
 """
prova1 = int(input("Digite a sua primeira nota(valendo 5): "))
prova2 = int(input("Digite a sua segunda nota(valendo 5): "))
prova3 = int(input("Digite a sua terceira nota(valendo 10): "))

media=(prova1 + prova2 + prova3)/2

if(media < 6):
    print("Sua média é",media,"e você foi reprovado.")

if(media >= 6):
    print("Sua média é",media,"e você foi aprovado.")