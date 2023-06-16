#!/usr/bin/python3
USAGE = "obe <filepath>"
space = {"LAST": None}


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


def run(action, arg1, arg2, arg3):
    global space
    if action == "print":
        print(arg1)
    elif action == "space":
        space[arg1] = arg2
    elif action == "join":
        space["LAST"] = arg1 + arg2
    elif action == "math":
        if arg2 == "+":
            space["LAST"] = str(int(arg1) + int(arg3))
        elif arg2 == "-":
            space["LAST"] = str(int(arg1) - int(arg3))
        elif arg2 == "*":
            space["LAST"] = str(int(arg1) * int(arg3))
        elif arg2 == "/":
            space["LAST"] = str(int(arg1) / int(arg3))
    elif action == "input":
        space["LAST"] = input(arg1)
    else:
        print(f"Error: Unknown Action \"{action}\"")


if __name__ == '__main__':
    import sys
    try:
        filepath = sys.argv[1]
        with open(filepath, "rt") as f:
            lines = f.readlines()
            for l in lines:
                parse(l.replace("\n", ""))
    except:
        print(f"Usage: {USAGE}")
