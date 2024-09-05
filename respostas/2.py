'''2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
'''
def quantas_letras_a(string):
    counter = 0
    
    for letra in string:
        if letra == 'a' or letra == 'A':
            counter += 1
    if counter == 0:
        print("A letra 'a' não está presente na string")
    else:
        print(f"A letra 'a' está presente na string {counter} vezes.")