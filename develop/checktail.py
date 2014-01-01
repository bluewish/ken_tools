#!/usr/bin/python

import os
import sys

def check_single_file (filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    for index in xrange(len(lines)):
        pos = len(lines[index]) - 1
        while pos >= 0:
            if ord(lines[index][pos]) in [0xa, 0xd]:
                pos = pos - 1
            else:
                break
        if pos < 0:
            continue
        if lines[index][pos] == " ":
            print "Found at line %d, colume: %d" % (index, pos)
            sys.exit(1)

def process (root_dir):
    for root, dirs, files in os.walk(root_dir):
        for path in dirs:
            if path.lower() in [".git", ".repo"]:
                dirs.remove(path)

        for path in files:
            full_path = os.path.join(root, path)
            print "scanning...", full_path
            check_single_file(full_path)

if __name__ == "__main__":
    print "Check current folder", os.getcwd()
    process(os.getcwd())
