#!/usr/bin/env python3

import pytest


def get_words(val):
    counts = {}
    words = val.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def given_input():
    x=1
    while x==1:
        try:
           
            val = input("Enter your text: ")
            print (get_words(val))
            exit =  input("press 0 to exit: ")
            
            if exit == '0':
                x = 0
                
        except ValueError:
            print("No.. input is not a number. It's a string")

if __name__ == '__main__':
    given_input()