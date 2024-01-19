#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(n):
    """task min operations"""
    num_operations = 0
    length = 1

    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                num_operations += i
                length *= i
                n //= i
                break
    return num_operations
