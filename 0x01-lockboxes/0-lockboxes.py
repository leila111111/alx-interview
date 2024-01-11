#!/usr/bin/python3
'''lockboxes'''


def canUnlockAll(boxes):
    '''method that determines
    if all the boxes can be opened.
    '''
    n = len(boxes)
    for i in range(0, n - 1):
        seen = False
        j = 0
        for find in boxes:
            if (i + 1) in find and (i + 1) != j:
                seen = True
                break
            j += 1
        if not seen:
            return False
    return True