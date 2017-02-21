#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse_size(size):
    if isinstance(size, basestring):
       sd = size.split('x')
    else:
       sd = size
    ws, hs = [int(x) for x in sd]

    return (ws, hs)

def colorbox(size, color):
    width, height = parse_size(size)
    return "%d x %d of %s" % (width, height, str(color))


# test functions

def test_x_y(x, y):
    assert(isinstance(x, int))
    assert(isinstance(y, int))
    print "x = %d, y = %d" % (x, y)


def test_size(size):
    x, y = parse_size(size)
    test_x_y(x, y)


def test():
    test_size((100, "20"))
    test_size(("100 ", " 22"))
    test_size("300x400")
    return 0

if __name__ == "__main__":
   import sys
   sys.exit(test())

