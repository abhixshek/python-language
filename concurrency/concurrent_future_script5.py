"""
implementing threading/concurrency using the concurrent.futures module
"""

#import threading
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping in {seconds} second...")
    time.sleep(seconds)
    return "Done sleeping..."


with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)

    print(f1.result()) # prints the returned value of the function
    print(f2.result())



#threads = []

#for _ in range(10): # we use _ to show that we are not really going to use the looping variable. its just a throw away variable. all we are about is looping 10 times not really using the variable.
#    t = threading.Thread(target=do_something, args=[1.5])
#    t.start()
#    threads.append(t)

#for thread in threads:
#    thread.join()



finish = time.perf_counter()

print(f'Finished in {finish - start:.2f} seconds.') # using .2f in strings is equivalent to using round(finish - start, 2)

