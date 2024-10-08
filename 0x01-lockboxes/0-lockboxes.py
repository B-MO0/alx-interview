#!/usr/bin/python3
"""Determines if all "boxes" can be unlocked"""


def canUnlockAll(boxes):
    """Returns True if all boxes have reachable key"""
    # Adds 0 to list
    key_list = [0]
    # Copies all keys in box 0
    test_key = boxes[0]
    # Follow every key along its path opening boxes
    # key is list of all available keys whether reachable or not
    for key in test_key:
        if key not in key_list:
            try:
                # Add keys from reachable box to test key list
                test_key.extend(boxes[key])
                key_list.append(key)
            except:
                continue
    # Return true if key_list contains key to all locked boxes
    if len(key_list) == len(boxes):
        return True
    return False