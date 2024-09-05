'''3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; 
enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?

RESPOSTA: soma = 77
'''

def soma_k(indice, k):
    soma = 0
    while k < indice:
        k += 1
        soma += k
    print(soma)

