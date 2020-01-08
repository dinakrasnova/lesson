#1
import re
import string
from typing import Any

text = open('text.txt', 'r', encoding = 'utf-8')
text = text.read()

text = (re.sub("[" + re.escape(string.punctuation) + "]", "", text))
print(text)

#2
list_temp = text
print(list_temp)

#3
list_temp = [element.lower() for element in list_temp]
print(list_temp)

#4

list_dict = {}
for i in range(len(list_temp)):
    list_dict[list_temp[i]] = list_temp.count(list_temp[i])
import operator
x = list_dict
list_dict = sorted(x.items(), key=operator.itemgetter(1), reverse = True)

#5

for i in range(5):
    print(list_dict[i])

my_set = set(list_temp)
print(my_set)


