#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(n):
    """task min operations"""
    operations = 0
    current_length = 1
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                operations += i
                current_length *= i
                n //= i
                break
    return operations

