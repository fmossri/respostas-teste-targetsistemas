'''2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
'''
def quantas_letras_a(string):
    counter = 0
    letras_a = ['a', 'A', 'á', 'Á', 'à', 'À', 'ã', 'Ã', 'â', 'Â']
    for letra in string:
        if letra in letras_a:
            counter += 1
    if counter == 0:
        print("A letra 'a' não está presente na string")
    else:
        print(f"A letra 'a' está presente na string {counter} vezes.")

string = "A string em questão possui 4 letras 'A'"
quantas_letras_a(string)