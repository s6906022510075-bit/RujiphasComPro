set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2)) #output: {1, 2, 3, 4, 5}

print(set1.intersection(set2))#output: {3}

print(set1.difference(set2))#output: {1, 2}

print(set1.symmetric_difference(set2))#output: {1, 2, 4, 5}