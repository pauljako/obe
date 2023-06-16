#!/usr/bin/python3

import os

# Set constants.
VERSION = "beta0.2"
USAGE = "obe <filepath>"
OBS_DIR = os.path.dirname(os.path.realpath("__file__"))

# Set Space to default.
space = {"LAST": None}


# Parses Code and Runs it.
def parse(code):
    global space
    spc = code.split(" ")
    action = spc[0]
    try:
        arg1 = spc[1].replace("§", " ")
        if arg1.startswith("$"):
            arg1 = space[arg1.replace("$", "")]
    except:
        arg1 = None
    try:
        arg2 = spc[2].replace("§", " ")
        if arg2.startswith("$"):
            arg2 = space[arg2.replace("$", "")]
    except:
        arg2 = None
    try:
        arg3 = spc[3].replace("§", " ")
        if arg3.startswith("$"):
            arg3 = space[arg3.replace("$", "")]
    except:
        arg3 = None
    run(action, arg1, arg2, arg3)


# Runs the code.
def run(action, arg1, arg2, arg3):
    global space
    if action == "print":
        print(arg1)
    elif action == "space":
        space[arg1] = arg2
    elif action == "join":
        space["LAST"] = str(arg1) + str(arg2)
    elif action == "math":
        if arg2 == "+":
            space["LAST"] = int(arg1) + int(arg3)
        elif arg2 == "-":
            space["LAST"] = int(arg1) - int(arg3)
        elif arg2 == "*":
            space["LAST"] = int(arg1) * int(arg3)
        elif arg2 == "/":
            space["LAST"] = int(arg1) / int(arg3)
    elif action == "input":
        space["LAST"] = input(arg1)
    elif action == "run":
        try:
            import os
        except:
            print("obe Error: Cannot import the os module.")
        try:
            space["LAST"] = os.system(arg1)
        except:
            print(f"Error: Error while running {arg1}")
    elif action == "quit":
        quit()
    elif action == "":
        pass
    else:
        print(f"Error: Unknown Action \"{action}\"")


if __name__ == '__main__':
    import sys
    try:
        # Display Version
        if sys.argv[1] == "-v" or sys.argv[1] == "--version":
            print(f"obe version: {VERSION}")
        # Read & Runs file
        else:
            try:
                filepath = os.path.join(OBS_DIR, sys.argv[1])
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
