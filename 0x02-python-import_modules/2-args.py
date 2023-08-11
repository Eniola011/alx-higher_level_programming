#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argmt = len(argv) - 1

    if argmt == 0:
        print("{} arguments.".format(argmt))
    elif argmt == 1:
        print("{} arguments:".format(argmt))
    else:
        print("{} arguments:".format(argmt))

    if argmt >= 1:
        argmt = 0
        for arg in argv:
            if argmt != 0:
                print("{}: {}".format(argmt, arg))
            argmt += 1
