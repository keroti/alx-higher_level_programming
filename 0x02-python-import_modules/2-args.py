#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) - 1) == 0:
        print("{} arguments.".format((len(sys.argv) - 1)))
    elif (len(sys.argv) - 1) == 1:
        print("{} argument.".format((len(sys.argv) - 1)))
        print("1: {}".format(sys.argv[0]))
    elif (len(sys.argv) - 1) >= 2:
        i = 0
        for i in range(len(sys.argv)):
            print("{} argument.".format((i + 1)))
            print("{}: {}".format((i + 1), sys.argv[i]))
            i += 1
