# Este código aborda a resistência à análise de tráfego, uma preocupação central no movimento cypherpunk. 
# A ideia é adicionar mensagens dummy (falsas) a um fluxo de comunicação para dificultar a identificação de padrões. 
# O código simula o envio de mensagens reais e dummy, misturando-as antes de exibi-las.
# Para executar, não são necessárias bibliotecas externas.

import random

def enviar_mensagens(mensagens_reais, num_dummy):
    mensagens_dummy = ["Mensagem Dummy"] * num_dummy
    todas_mensagens = mensagens_reais + mensagens_dummy
    random.shuffle(todas_mensagens)
    return todas_mensagens

mensagens_reais = ["Olá, como você está?", "Vamos nos encontrar amanhã?", "A reunião foi adiada."]
num_dummy = 5

resultado = enviar_mensagens(mensagens_reais, num_dummy)
print("Mensagens enviadas:")
for msg in resultado:
    print(msg)