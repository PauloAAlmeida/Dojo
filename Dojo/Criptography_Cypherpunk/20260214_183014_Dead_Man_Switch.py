# Este código implementa um "Dead Man Switch", que executa uma ação caso um check-in falhe. 
# O usuário deve se "check-in" periodicamente. Se o check-in não for feito dentro de um tempo limite, 
# o código executa uma ação (neste caso, imprime uma mensagem de alerta). 
# Para rodar, não são necessárias bibliotecas externas.

import time
import threading

def check_in():
    global last_check_in
    while True:
        last_check_in = time.time()
        print("Check-in realizado.")
        time.sleep(5)  # Check-in a cada 5 segundos

def dead_man_switch():
    while True:
        time.sleep(10)  # Tempo limite de 10 segundos para o check-in
        if time.time() - last_check_in > 10:
            print("ALERTA: Check-in falhou! Executando ação de emergência.")
            break

last_check_in = time.time()
threading.Thread(target=check_in, daemon=True).start()
dead_man_switch()