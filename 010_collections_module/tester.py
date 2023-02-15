from collections import Counter

sample_string = 'aaaaaaaaaabbbbbbbbccccccccccccdddddddeeee'

my_counter = Counter(sample_string)
print(type(my_counter))
print(my_counter)
print(my_counter['b'])

print(my_counter.keys())
print(my_counter.values())
print(my_counter.items())

print(my_counter.most_common(2))
print(my_counter[1][1])
