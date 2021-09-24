#!/usr/bin/python3
# Simple script to show how arguments are passed to python

import sys
from tictok import slow_print


if __name__ == "__main__":
    args = sys.argv
    print("Arguments passed to this script:")
    print(args)

    if len(args) > 2:
        msg = str(args[2])
        times = int(args[1])
        slow_print(n=times, msg=msg)
    elif len(args) > 1:
        slow_print(int(args[1]))
    else:
        slow_print()
    
