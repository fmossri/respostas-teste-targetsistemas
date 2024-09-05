'''
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas
diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar 
os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla 
qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas 
das lâmpadas, qual interruptor controla cada lâmpada? 
'''

'''
  Primeiro ligo o interruptor 1 e espero alguns minutos para que a lâmpada correspondente 
esquente. Em seguida aciono o interruptor 2, e vou à sala "A". Se a lâmpada estiver
acesa, ela corresponde ao interruptor 2; se estiver apagada, mas quente, ao 
interrutpor 1; e se estiver apagada e fria, ao interruptor 3.
  Com apenas duas correspondências desconhecidas, volto à sala dos interruptores. Se a 
sala "A" corresponder ao interruptor 2, desligo-o, 
ligo o interruptor 1 novamente e vou à sala "B". Caso contrário, apenas deixo 
os interrutptores como estão e vou à sala "B" para verificar se sua lâmpada está acesa.
  Dessa forma consigo determinar a correspondência entre cada interruptor e cada sala.
'''