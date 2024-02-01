#!/usr/bin/python3
"""UTF-8 Validation
"""


def validUTF8(data):
    """method that determines if a given data set represents
    a valid UTF-8 encoding."""
    count_bits = 0
    for i in range(len(data)):
        if count_bits == 0:
            bits = 0
            decal = 1 << 7
            while decal & data[i]:
                bits += 1
                decal = decal >> 1
            count_bits = bits
            if count_bits == 0:
                continue
            if count_bits == 1 or count_bits > 4:
                return False
        else:
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        count_bits -= 1
    return count_bits == 0
