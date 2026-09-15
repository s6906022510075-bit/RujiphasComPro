set_a = {1, 2, 3, 4}
set_b = {2,3}
set_c = {1, 2, 3, 4}
set_d = {1, 2, 3, 4, 5}

print("is set_a a superset of set_b?", set_a >= set_b)  # Output: True
print("is set_b a subset of set_a?", set_b <= set_a)  # Output: True

print("is set_a a proper superset of set_b?", set_a > set_b)  # Output: True
print("is set_b a proper subset of set_a?", set_b < set_a)  # Output: True

print("Are set_b and set_c equal?", set_b == set_c)  # Output: False
print("Are set_a and set_c equal?", set_a == set_c)  # Output: True

print("is set_b a subset of set_d and not equal to it?", set_b <= set_d and set_b != set_d)  # Output: True