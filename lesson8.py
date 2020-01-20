#1. Написать декоратор, замеряющий время выполнение декорируемой функции
import time
import requests
import os
import random
import psutil

def show_time(f):

    def wrapper(*args, **kwargs):
        print(time.time())
        print('URL: ', args[0])
        text = f(*args, **kwargs)
        print(time.time())
        return text
    return wrapper

@show_time
def requests_example(url):
    webpage = requests.get(url)
    return webpage.text

url = 'https://google.com'

text = requests_example(url)

print(text)

#2. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).

number = list(range(1, 1000000))

def numbs(num):
    nums_list = []
    for i in range(num):
        num = {'number': random.choice(num),
               'id':i}
        nums_list.append(num)
    return nums_list
proc = psutil.Process(os.getpid())
print('Исп. память до вып. функции:' + str(proc.memory_info().rss/1000000))
start=time.clock()
nums_list = numbs(1000000)
stop=time.clock()
proc=psutil.Process(os.getpid())
print('Исп. память после вып. функции:'+str(proc.memory_info().rss/1000000))
print("Заняло {} секунд".format(stop-start))


# Применим генератор!
'''
def numbs_gen(num):
    for i in range(num):
        num = {'number': random.choice(num),
               'id': i}
        yield num


proc = psutil.Process(os.getpid())

print('Исп. память до вып. функции:' + str(proc.memory_info().rss/1000000))
start=time.clock()
nums_generator = numbs_gen(1000000)
stop=time.clock()

proc=psutil.Process(os.getpid())
print('Исп. память после вып. функции:'+str(proc.memory_info().rss/1000000))
print("Заняло {} секунд".format(stop-start))
'''