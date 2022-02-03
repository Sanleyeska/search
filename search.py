#!/bin/python3
#-*-coding:utf-8-*-
import sys, os
browser = "firefox"
if len(sys.argv) <= 2:
    print("Error, run: ./search.py a b")
else:
    print("Searching: {} {}".format(sys.argv[1], sys.argv[2]))
    os.system("{} https://www.google.com/search?q={}+{}".format(browser, sys.argv[1], sys.argv[2]))
