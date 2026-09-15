set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1 &= set2
print("After intersection update:", set1)  # Output: {4, 5}

set1 = {1, 2, 3, 4, 5}

set1 |= set2
print("After union update:", set1)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

set1 = {1, 2, 3, 4, 5}
set1 -= set2
print("After difference update:", set1)  # Output: {1, 2, 3}

set1 = {1, 2, 3, 4, 5}
set1 ^= set2
print("After symmetric difference update:", set1)  # Output: {1, 2, 3, 6, 7, 8}


