"""
implementing threading/concurrency using the concurrent.futures module
and using map() built-in function to loop through our list and apply the executor.submit() method on them.
"""

#import threading
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping in {seconds} second...")
    time.sleep(seconds)
    return f"Done sleeping..{seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds_of_sleep = [5, 2, 4, 3, 1]
    results = executor.map(do_something, seconds_of_sleep) # executor.map() returns the results of our passed in iterator in the order of the items that were passed. 
    # this is different from the previous example where we got the futures object from executor.submit() and then looped through the as_completed threads.
    # note that the code is still running concurrently and the time of our script is going to be the same as the last example. 

    for result in results:
        print(result)

# NOTE When using the context manager, the context manager does not end until all the threads have been completed. Unlike the 1st few examples (see script2.py) that we looked at using the threading module where if you didnt join the threads the script printed finished in 0 seconds even though the actual script run time was still taking into consideration the fact that the script cannot end until the threads have all been completed.
    
finish = time.perf_counter()

print(f'Finished in {finish - start:.2f} seconds.') # using .2f in strings is equivalent to using round(finish - start, 2)

