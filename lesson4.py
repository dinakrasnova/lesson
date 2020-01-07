# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
#(могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
from random import choices

def choice_name(names, len_list):
    return choices(names, k=len_list)

my_list = choice_name(['Kate', 'Adam', 'Nataly', 'Lisa', 'John', 'Kate', 'Olga', 'Maria', 'Artem', 'Julia', 'Olga', 'Lisa', 'Maria', 'Alex', 'Peter', 'Julia', 'Andrew', 'Kate', 'Sam', 'Garry'], len_list=100)
print(my_list)

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;

def most_frequent(names):
    word = {}
    for name in names:
        word[name] = word.get(name, 0) + 1
    word = list(word.items())
    word.sort(key=lambda x: x[1], reverse=True)
    return word[0][0]

print(most_frequent(my_list))

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
def less_letters(names):
    letters = {}
    for name in names:
        for char in name:
            letters[char] = letters.get(char, 0) + 1
    letters = sorted(list(letters.items()), key=lambda x: x[1])
    return letters[0][0]
print(less_letters(my_list))