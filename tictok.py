#!/usr/bin/python3
from time import sleep
import sys

def slow_print(n=10, msg="hello world"):
    """ print msg repeatedly """
    for i in range(n):
        sleep(1)
        try:
            print(f"STDOUT: {msg} - {i}", flush=True)
        except (IOError, BrokenPipeError):
            # close and terminate if stdout no longer accepting output
            sys.stderr.close()
            exit()



if __name__ == "__main__":
    slow_print()
    
