from threading import Thread, Lock

number = 0
data_lock = Lock()

def IncrementNumber():
    global number
    for i in range (0, 10000):
        data_lock.acquire()
        number = number + 1
        print(number)
        # Se não colocar um data_lock.release() aqui, liberando o mutex manualmente, a thread ficará presa nessa região crítica causando um deadlock

t1 = Thread(target=IncrementNumber)
t2 = Thread(target=IncrementNumber)
t3 = Thread(target=IncrementNumber)
t4 = Thread(target=IncrementNumber)
t5 = Thread(target=IncrementNumber)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()