 """ # 33) Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
códigos utilizados são:
 1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
valor zero. """

js = 0 
ja = 0
ac = 0
pe = 0
vn = 0
vb = 0
total = 0 
while True:
    cand = int(input("Votos\n"
                "---------\n"
                    "1 - Jose\n"
                    "2 - João\n"
                    "3 - Aquele cara\n"
                    "4 - Pedro\n"
                    "5 - Voto Nulo\n"
                    "6 - Voto em Branco\n"
                    "7 - Sair\n"
                    ": "))
    total = js+ja+ac+pe+vn+vb
    
    if cand == 1:
        js += 1
    elif cand == 2:
        ja +=  1
    elif cand == 3:
        ac += 1
    elif  cand == 4:
        pe += 1
    elif cand == 5:
        vn += 1
    elif cand == 6:
        vb += 1
    
    if cand == 7:
        x = (vb*100)/ total
        y = (vn*100)/ total
        print(f"Jose = {js}\n"
              f"João = {ja}\n"
              f"Aquele cara = {ac}\n"
              f"Pedro = {pe}\n"
              f"Voto Nulo = {vn}\n"
              f"Voto em Branco = {vb}\n"
              f"Porcentagem de votos brancos = {x}\n"
              f"Porcentagem de votos nulos = {y}")
        break

