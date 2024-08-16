import threading
import time
import random


N = 5

hashis = [threading.Semaphore(1) for _ in range(N)]

def comer(filosofo):
    print(f"Filósofo {filosofo} está comendo")
    time.sleep(random.randint(2, 4)) 
    print(f"Filósofo {filosofo} terminou de comer")

def pensar(filosofo):
    print(f"Filósofo {filosofo} está pensando")
    time.sleep(random.randint(2, 4)) 
    print(f"Filósofo {filosofo} terminou de pensar")

def pegar_hashis(filosofo):
    hashis[(filosofo - 1) % N].acquire()
    print(f"Filósofo {filosofo} pegou o hashi à esquerda")

    hashis[filosofo % N].acquire()
    print(f"Filósofo {filosofo} pegou o hashi à direita")

def soltar_hashis(filosofo):
    hashis[filosofo % N].release()
    print(f"Filósofo {filosofo} soltou o hashi à direita")
    hashis[(filosofo - 1) % N].release()
    print(f"Filósofo {filosofo} soltou o hashi à esquerda")

def filosofo(filosofo):
    while True:
        pensar(filosofo)
        pegar_hashis(filosofo)
        comer(filosofo)
        soltar_hashis(filosofo)

threads = []
for i in range(N):
    t = threading.Thread(target=filosofo, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()