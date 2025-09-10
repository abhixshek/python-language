import time
reps = 1000
repslist = range(reps) # this is contructed outside the timing loop, so that its contruction time is not added. In python 3, range() is an iterator so this step isnt required, but doesnt hurt.

def timer(func, *pargs, **kargs):
    start = time.time()
    for i in repslist:
        res = func(*pargs, **kargs)
    elapsed = time.time() - start
    return (elapsed, res)

