# Multithreading - A thread is an independent flow of execution, A single process consist of multiple threads.
# Each thread in a program perform a particular task. Each process has 1 thread that is always running, this thread 
# is now as main thread. The main thread creates the child thread objects. The child thread is also initiated by the main thread.
# Mutithreading is very useful for saving time & improving performance.

# Multithreading can only be used when dependency between indivisual threads does not exist.

from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(500):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(500):
            print("Hi")
            sleep(1)

# Both thread will run parallely this is multitasking.
t1 = Hello()
t2 = Hi()

# gave 0.2 sec differece to avoid collision in parallel execution of t1 and t2.
t1.start()
sleep(0.2)  
t2.start()

# This is to make main thread print at last.
t1.join()
t2.join()

# This will be printed by main thread.
print("BYE")

