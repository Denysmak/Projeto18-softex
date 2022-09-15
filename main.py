#Desenvolva um programa que recebe do usuário nome completo e ano de
#nascimento que seja entre 1922 e 2021. A partir dessas informações, o
#sistema mostrará o nome do usuário e a idade que completou, ou completará
#, no ano atual(2022).
#Caso o usuário não digite um número ou apareça um inválido no campo do ano
#, o sistema informará o erro e continuará perguntando até que um valor correto
#seja preenchido.
#
def idade():
    erro = False
    while(erro == False):
        nome = input("Escreva o seu nome: ")
        ano = int(input("Escreva o seu ano de nascimento: "))
        idade = 2022 - ano
        try:
            if(ano >= 1922 and ano <= 2021):
                print("numero válido")
                erro = True
                print("O seu nome é " + nome + " e você tem " + str(idade) + " anos")
        except:
            print("teste")


idade()