#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argmt = len(sys.argv) - 1

    if argmt == 0:
        print("{} arguments.".format(argmt))
    elif argmt == 1:
        print("{} arguments:".format(argmt))
    else:
        print("{} arguments:".format(argmt))

    if argmt >= 1:
        argmt = 0
        for arg in sys.argv:
            if argmt != 0:
                print("{}: {}".format(argmt, arg))
            argmt += 1
