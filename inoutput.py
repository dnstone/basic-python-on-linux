#!/usr/bin/python3
# Expect input and generates output to demonstrate STDIN, STDOUT, STDERR
# Run --help to get basic information on how to run
# Example: ./inoutput.py -p 3 msg1 "message 2"
# 
import sys
from warnings import warn
import argparse

# sys package in python has more low level access to the STDIN, STDOUT, STERR
def sys_io(n, msg1, msg2):
    """Show io using sys"""
    for i in range(n):
        stdin = sys.stdin.readline().strip()
        display_msg = f"\nSTDOUT: info - your STDIN input was '{stdin}'\n"
        sys.stdout.write(display_msg)
        sys.stdout.write(f"STDOUT: {msg1}\n")
        sys.stderr.write(f"STDERR: {msg2} in loop #{i}\n")

# runs when -p is supplied as option/argument
def python_io(n, msg1, msg2):
    """show io using some common python functions like print and input"""
    for i in range(n):
        # normal python commands that use these buffers:
        stdin = input("\nenter an input in STDIN:")     # prints prompt message to STDOUT and retrieves STDIN
        display_msg = f"STDOUT: info - your STDIN input was '{stdin}'"
        print(display_msg)    # STDOUT
        print(f"STDOUT: {msg1}")    #STDOUT
        warn(f"STDERR: {msg2} in loop #{i}")     #STDERR



if __name__ == "__main__":
    # set up parser to parse command line arguments (not important part)
    parser = argparse.ArgumentParser(description="Python script demonstrating utilizing input and output")
    parser.add_argument('-p', action='store_true', help='use python version')
    parser.add_argument('n', nargs='?',  action='store', type=int, default=1, help="number of times to loop for input")
    parser.add_argument('msg1', nargs='?', action='store', type=str, default="1 stdout default msg", help="msg for STDOUT")
    parser.add_argument('msg2', nargs='?', action='store', type=str, default="2 stderr default msg", help="msg for STDERR")
    args = parser.parse_args()
    if args.p:
        python_io(args.n, args.msg1, args.msg2)
    else:
        sys_io(args.n, args.msg1, args.msg2)


