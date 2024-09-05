'''1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre 
    será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
    escreva um programa na linguagem que desejar onde, informado um número, ele calcule
    a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
    pertence ou não a sequência.'''

def esta_na_fibonacci(numero):
    f_0 = 0
    f_1 = 1
    soma = 0
    while soma <= numero:
        soma = f_0 + f_1
        if soma == numero:
            return "numero está na fibonnaci"

        f_0 = f_1
        f_1 = soma
        
    return "o número não está na fibonacci"
