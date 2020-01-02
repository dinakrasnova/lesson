#1
import re
valids = re.sub(r"[^A-Za-zА-Яа-я]+", '', 'Hello,!?')
print(valids)

#2
list_temp = ['Orange', 'apple', 'Grape', 'orange', 'Cherry']
print(list_temp)

#3
list_temp = [element.lower() for element in list_temp]
print(list_temp)

#4

key_lst = ['orange', 'apple', 'grape', 'orange', 'cherry']
value_lst = [2, 1, 1, 2, 1]
my_dict = dict(zip(key_lst, value_lst))
print(my_dict)

#5

my_list = ['orange', 'apple', 'grape', 'orange', 'cherry', 'apple', 'melon', 'grape', 'cherry']
my_list.sort(reverse = True)
print(my_list)

my_set = set(my_list)
print(my_set)


