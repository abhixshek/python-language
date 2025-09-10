"""
timer(spam, 1, 2, a=3, b=4, _reps=1000) calls and times spam(1, 2, a=3)
_reps times, and returns total time for all runs, with final result;
best(spam, 1, 2, a=3, b=4, _reps=50) runs best-of-N timer to filter out
any system load variation, and returns best time among _reps tests
"""
import time
import sys


def trace(*args):
    pass # or print args

def timer(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)
    trace(func, pargs, kargs, _reps)
    repslist = range(_reps)
    start = time.time()
    for i in repslist:
        res = func(*pargs, **kargs)
    elapsed = time.time() - start
    return (elapsed, res)

def best(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 50)
    trace(func, pargs, kargs, _reps)
    repslist = range(_reps)
    best = 2 ** 32
    for i in repslist:
        start = time.time()
        res = func(*pargs, **kargs)
        elapsed = time.time() - start
        if elapsed < best: best = elapsed
    return (best, res)

def timer_new(func, *pargs, _reps=100, **kargs): # timer_new is same as timer, but uses keyword-only arguments of python 3.0 to handle _reps
    trace(func, pargs, kargs, _reps)
    start = time.time()
    for i in range(_reps):
        res = func(*pargs, **kargs)
    elapsed = time.time() - start
    return (elapsed, res)


