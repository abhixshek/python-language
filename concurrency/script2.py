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
t2.start()


finish = time.perf_counter()

print(f'Finished in {finish - start:.2f} seconds.') # using .2f in strings is equivalent to using round(finish - start, 2)

# script takes 2 seconds as expected

