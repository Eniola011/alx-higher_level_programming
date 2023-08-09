#!/usr/bin/python3
for alp in reversed(range(97, 123)):
    print("{:c}".format(alp if (alp % 2 == 0) else (alp - 32)), end='')
