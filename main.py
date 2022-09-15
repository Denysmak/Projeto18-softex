def idade():
    Rodando = True
    while(Rodando == True):
        nome = input("Escreva o seu nome: ")
        ano = int(input("Escreva o seu ano de nascimento: "))
        idade = 2022 - ano
        try:
            if(ano >= 1922 and ano <= 2021):
                print("numero válido")
                Rodando = False
                print("O seu nome é " + nome + " e você tem " + str(idade) + " anos")
        except:
            print("teste")


idade()
