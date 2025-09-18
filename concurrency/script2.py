"""
Lets convert our 2 function calls into 2 threads.
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
print(f"Count of active threads: {threading.active_count()}") # prints 2, because one is the MainThread which is always run whenever we execute python code.
t2.start()
print(f"Count of active threads: {threading.active_count()}")


finish = time.perf_counter()

print(f'Finished in {finish - start:.2f} seconds.') # using .2f in strings is equivalent to using round(finish - start, 2)

# script takes 0.00 seconds as expected. # but this is because our calculation is not taking into account the finishing of the threads. see script3 for solution

