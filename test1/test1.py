#!/usr/bin/env python3

import pytest

def mult_5(x):
    return x % 5 == 0

def mult_3(x):
    return x % 3 == 0

def mult_35(x):
    return x % 5 == 0 and x % 3 == 0

def test_calc_multiples():
    numbers = [i for i in range(1,100)]
    for n in numbers:
        if mult_35(n):
           print ('fizz buzz')
        elif mult_5(n):
           print ('fizz')
        elif mult_3(n):
           print ('buzz')
        else:
            print (n) 

        


if __name__ == '__main__':
    test_calc_multiples()
    