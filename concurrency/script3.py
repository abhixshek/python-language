"""
Lets convert our 2 function calls into 2 threads. And join them so that the script run time is calculated only after all function runs/threads have finished.
"""

import threading
import time

start = time.perf_counter()

def do_something():
    print("Sleeping in 1 second...")
    time.sleep(1)
    print("Done sleeping...")


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

# do_something()
# do_something()

t1.start()
t2.start()

# to make sure our function runs are complete before calculating the finish time we run join on the threads
t1.join()
t2.join()
# NOTE, thread.join() will cause the program to pause until the thread we started completed.

finish = time.perf_counter()

print(f'Finished in {finish - start:.2f} seconds.') # using .2f in strings is equivalent to using round(finish - start, 2)

# script takes 1.01 seconds as expected

