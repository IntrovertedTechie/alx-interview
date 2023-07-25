#!/usr/bin/python3
"""
UTF-8 Validation module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    num_bytes_to_process = 0

    for num in data:
        byte = num & 0xFF  # Consider only the 8 leasr

        if num_bytes_to_process == 0:
            if (byte >> 7) == 0:  # 1-byte character
                continue
            elif (byte >> 5) == 0b110:  # 2-byte character
                num_bytes_to_process = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes_to_process = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes_to_process = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:  # Check if it's a continuation byte
                return False
            num_bytes_to_process -= 1

    return num_bytes_to_process == 0
