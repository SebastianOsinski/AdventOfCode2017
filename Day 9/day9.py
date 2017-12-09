# pylint: disable=invalid-name
import sys
import os

path = os.path.join(sys.path[0], "day9_input")
file = open(path, "r")

stream = file.readline()

def total_score(stream):
    GROUP_OPEN = '{'
    GROUP_CLOSE = '}'
    GARBAGE_OPEN = '<'
    GARBAGE_CLOSE = '>'
    IGNORE = '!'

    current_score = 0

    current_level = 0

    should_ignore = False
    is_in_garbage = False

    garbage_count = 0

    for char in stream:
        if should_ignore:
            should_ignore = False
            continue

        if is_in_garbage:
            if char == IGNORE:
                should_ignore = True
            elif char == GARBAGE_CLOSE:
                is_in_garbage = False
            else:
                garbage_count += 1
            continue
        
        if char == GROUP_OPEN:
            current_level += 1
        elif char == GROUP_CLOSE:
            current_score += current_level
            current_level -= 1
        elif char == GARBAGE_OPEN:
            is_in_garbage = True
        
    return (current_score, garbage_count)


print(total_score(stream))