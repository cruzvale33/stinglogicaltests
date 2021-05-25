#!/usr/bin/env python3

import pytest

def calc_fibonacci(nterms):
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    else:
        print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

def solve_fibonacci():
    x=1
    while x==1:
        try:
            # Convert it into integer
            val = int(input("Enter your value: "))
            val = 10
            calc_fibonacci(val)
            exit =  input("press 0 to exit: ")
            
            if exit == '0':
                x = 0
               
        except ValueError:
            print("No.. input is not a number. It's a string")
       

if __name__ == '__main__':
    solve_fibonacci()