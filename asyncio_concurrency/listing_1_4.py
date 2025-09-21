"""
Use multiprocessing module to create multiple processes, instead of multiple threads like in the previous script.
The API is similar to that of `threading` module.
"""
import os
import multiprocessing


def hello_from_process():
    print(f"Hello from child process: {os.getpid()}!")

if __name__ == "__main__":
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()

    print(f"Hello from parent process: {os.getpid()}")

    hello_process.join() # waits for the hello_process to complete before proceeding further from here

