set_1 = {'books', 'author', 'code', 'numbers'}
set_2 = {'names', 'age', 'gender', 'phone_number'}

diff = set_2.difference(set_1)
diff = set_2.intersection(set_1)
diff = set_2.union(set_1)
print(diff)

l = [1,2,3,4,5,6,7,8,9,'abc','bcd']

no_duplicate_set = set(l)
print(no_duplicate_set)

no_duplicate_set.add('lawrence')
print(no_duplicate_set)