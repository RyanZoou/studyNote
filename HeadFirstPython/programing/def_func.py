# -*- coding: utf-8 -*-

#this file show a function how to get result for 'ax2 + bx + c = 0'

import math

def quadratic(a, b, c):
    result = 0
    if a == 0:
        return - c/b
    else:
        if b**2 - 4*a*c < 0:
            return 'This params can\'t get a result!'
        else:
            result = (math.sqrt((b**2 - 4*a*c)/4*a*a) - b/(2*a),- math.sqrt((b**2 - 4*a*c)/4*a*a) - b/(2*a))
    return result

# print(quadratic(8,91,46))

def testParams(*list):
    sum = 0
    for n in list:
        sum += n
    return sum

list = [1,2,3,4,5,6,7,8,9,10]

print(testParams(1,4,8,3))