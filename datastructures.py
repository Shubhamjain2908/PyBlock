simple_list = [1,2,3,4]
simple_list.extend([5,6,7])
del(simple_list[0])
print(simple_list)

dictionary = {'name': 'SJ'}
print(dictionary.items())
for k, v in dictionary.items():
    print(k, v)
del(dictionary['name'])
print(dictionary)

tup = (1,2,3) # immutable (cannot be changed)
print(tup.index(1))

sett = {'Shubham', 'Max', 'John', 'Shubham'}
# del(s['Shubham']) (use discard)
print(sett)

#Special Cases#
new_list = [True,True,False]
print(any(new_list)) # True
print(all(new_list)) # False

# Use case: checking if all no are positive
number_list = [1,2,3,4,-5]
# number_list > 0 -> error
print(all([el>0 for el in number_list]))
print(any([el>0 for el in number_list]))
