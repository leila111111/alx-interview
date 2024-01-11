#!/usr/bin/python3
'''lockboxes'''


def canUnlockAll(boxes):
    '''method that determines
    if all the boxes can be opened.
    '''
    unlocked = [False]
    unlocked[0] = True

    for keys in boxes:
        for key in keys:
            if 0 <= key < len(boxes):
                unlocked[key] = True

    return all(unlocked)