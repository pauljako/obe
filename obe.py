#!/usr/bin/python3

import os 
import inspect

# Set constants.
VERSION = "beta0.3"
USAGE = "obe <filepath>"
OBE_DIR = os.path.dirname(os.path.realpath("__file__"))
OBE_NAME = inspect.getframeinfo(inspect.currentframe()).filename
PATH = os.path.dirname(os.path.abspath(OBE_NAME))

# Set Space to default.
space = {"LAST": None}


# Runs the code.
def run(action, args, space):
    if action == "print":
        print(args[0])
    elif action == "space":
        space[args[0]] = args[1]
    elif action == "join":
        space["LAST"] = str(args[0]) + str(args[1])
    elif action == "input":
        space["LAST"] = input(args[0])
    elif action == "run":
        try:
            space["LAST"] = os.system(args[0])
        except:
            print(f"Error: Error while running {args[0]}")
    elif action == "quit":
        quit()
    elif action == "replace":
        space["LAST"] = args[0].replace(args[1], args[2])
    elif action == "":
        pass
    else:
        print(f"Error: Unknown Action \"{action}\"")
    return space


# Parses Code and Runs it.
def parse(code):
    global space
    spc = code.split(" ")
    action = spc[0]
    args = []
    args_unformatted = spc[1:]
    for a in args_unformatted:
        e = a.replace("§", " ")
        if e.startswith("$"):
            e = space[e.replace("$", "")]
        args.append(e)
    space = run(action, args, space)


if __name__ == '__main__':
    import sys
    try:
        # Display Version
        if sys.argv[1] == "-v" or sys.argv[1] == "--version":
            print(f"obe version: {VERSION}")
        elif sys.argv[1] == "-p" or sys.argv[1] == "--path":
            print(f"obe path: {PATH}")
        # Read & Runs file
        else:
            try:
                filepath = os.path.join(OBE_DIR, sys.argv[1])
                with open(filepath, "rt") as f:
                    lines = f.readlines()
                    try:
                        for l in lines:
                            parse(l.replace("\n", ""))
                    except:
                        print("An Unknown Error occurred")
            except:
                print(f"Error: cannot load file \"{filepath}\"")
    except:
        print(f"Usage: {USAGE}")
