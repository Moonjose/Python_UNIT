from threading import Thread, Lock

counter = 0
data_lock = Lock()

# Method created to simulate race condition once python 3.10 introduced an optimisation patch that changes eval breaking methods in GIL
def returnOne(): return 1 

# Race Condition way
# def increment():
#     global counter
#     for i in range(1000000):
#         counter += returnOne()

# Solution
def increment():
    global counter
    local_counter = 0
    for _ in range(1000000):
        local_counter += 1
    with data_lock: #Automatically aquire and release the mutex 
        counter += local_counter

threads = []
for i in range(10):
    t = Thread(target=increment)
    threads.append(t)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"The final counter value is {counter}")



