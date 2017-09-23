"""
Fuel Injection Perfection
=========================

Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly.

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.

The fuel control mechanisms have three operations:

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called answer(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
answer(4) returns 2: 4 -> 2 -> 1
answer(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

Test cases
==========

Inputs:
    (string) n = "4"
Output:
    (int) 2

Inputs:
    (string) n = "15"
Output:
    (int) 5
"""


def to_binary(number):
    return '{0:b}'.format(number)


def to_number(string):
    return int(string, 2)


def increment(binary):
    new_binary = list(binary)
    i = len(binary) - 1
    stop = False
    while stop is False and i >= 0:
        if binary[i] == '1':
            new_binary[i] = '0'
            i = i-1
        else:
            new_binary[i] = '1'
            stop = True
    if i < 0:  # we flipped bits until the beginning
        new_binary = ['1'] + new_binary
    return ''.join(new_binary)


def decrement(binary):
    new_binary = list(binary)
    i = len(binary) - 1
    stop = False
    while stop is False and i >= 0:
        if binary[i] == '1':
            new_binary[i] = '0'
            stop = True
        else:
            new_binary[i] = '1'
            i = i-1
    if i == 0:
        new_binary = new_binary[1:]
    return ''.join(new_binary)


def decrement_or_increment(binary):
    d = decrement(binary)
    i = increment(binary)
    return sorted([(d, d[::-1]), (i, i[::-1])], key=lambda x: x[1])[0][0]  # prefer the one with the most trailing zeros


def answer(s):
    total_operations = 0
    s = to_binary(long(s))
    while s != '1' and s != '11':  # if number = 3, just substract 2 times instead of doing the algorithm
        if s[-1] == '0':
            s = s[:-1]
        else:
            s = decrement_or_increment(s)
        total_operations += 1
    if s == '11':
        total_operations += 2
    return total_operations