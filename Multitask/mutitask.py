# mutitask.py
import time
import threading

def a():
    for i in range(10):
        print('Shower...'
        )
        time.sleep(0.5)
def b():
    for i in range(10):
        print('Tootbload...')
        time.sleep(0.5)
task1 = threading.Thread(target=a)
task2 = threading.Thread(target=b)
task1.start()
task2.start()
task1.join()
task2.join()

# a()
# b()
