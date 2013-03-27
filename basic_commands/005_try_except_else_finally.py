import sys


def cat(filename):
    f = None
    try:
        f = open(filename)
    except IOError:
        print "could not open the file"
    else:
        for line in f:
            print line,
    finally:
        if f:
            f.close()


if len(sys.argv) == 2:
    cat(sys.argv[1])
