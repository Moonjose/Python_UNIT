from threading import Thread, Lock

number = 0

def IncrementNumber():
    global number
    for i in range (0, 10000):
        number = number + 1
        print(number)


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