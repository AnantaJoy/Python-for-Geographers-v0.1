lottery_ticket = {3, 5, 17, 11, 21, 29, 31,11, 5}
print(lottery_ticket) 


# Sets are unordered, so you cannot access them with an index.
# print(lottery_ticket[0]) # TypeError: 'set' object is not subscriptable

# Sets are mutable, so you can add or remove items.

group_A = {'Ava', 'Olivia', 'Ethan', 'Mia', 'Mason', 'Liam', 'Noah', 'Emma', 'Sophia', 'Isabella'}
group_B = {'Mia', 'Mason', 'Liam', 'Noah', 'Emma', 'Sophia', 'Isabella', 'Ava', 'Olivia', 'Ethan'}

# Add an item to a set
group_A.add('James')
print(group_A)

# Remove an item from a set
group_A.remove('James')
print(group_A)

# Remove an item from a set without raising an error if it is not present
group_A.discard('James')
print(group_A)

# Union of two sets
print(group_A | group_B)
print(group_A.union(group_B))

# Intersection of two sets
print(group_A & group_B)
print(group_A.intersection(group_B))

group_A = {3,4,5,6,7}
group_B = {3,6,7,8,9,10}

# Symmetric difference of two sets
print(group_A ^ group_B)
print(group_A.symmetric_difference(group_B))

# Difference of two sets
print(group_A - group_B)

