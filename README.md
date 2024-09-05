# Teste técnico da Target Sistemas
Perguntas e respostas do teste

---

## 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
### **IMPORTANTE**: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
### [`Resposta da Questão 1`](https://github.com/fmossri/respostas-teste-targetsistemas/blob/main/respostas/1.py)

---

## 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

### IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
### [`Resposta da Questão 2`](https://github.com/fmossri/respostas-teste-targetsistemas/blob/main/respostas/2.py)

---

## 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA); Ao final do processamento, qual será o valor da variável SOMA?
### `77`

## 4) Descubra a lógica e complete o próximo elemento:
### a) `9`
### b) `128`
### c) `49`
### d) `100`
### e) `13`
### f) `200`


## 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

Primeiro ligo o interruptor 1 e espero alguns minutos para que a lâmpada correspondente esquente. Em seguida aciono o interruptor 2 e vou à sala "A". Se a lâmpada estiver acesa, ela corresponde ao interruptor 2; se estiver apagada, mas quente, ao interruptor 1; e se estiver apagada e fria, ao interruptor 3.

Com apenas duas correspondências desconhecidas, volto à sala dos interruptores. Se a sala "A" corresponder ao interruptor 2, desligo-o, ligo o interruptor 1 novamente e vou à sala "B". Caso contrário, apenas deixo os interruptores como estão e vou à sala "B" para verificar se sua lâmpada está acesa.

Dessa forma consigo determinar a correspondência entre cada interruptor e cada sala.
