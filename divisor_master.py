import math
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами)

def IsPrime(n):
   d = 2
   while n % d != 0:
       d += 1
   return d == n

print(IsPrime(48))

#2) выводит список всех делителей числа;
def get_ls(n):
    """Разложить число на множители"""
    #result = [1]
    result = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            n //= i
            result.append(i)
        else:
            i += 1
    if n > 1:
        result.append(n)
    return result
print (get_ls(16))

#3) выводит самый большой простой делитель числа

def issimple(a):
    r=math.ceil(math.sqrt(a))
    lst=[]
    for i in range(3,r):
        if a%i==0:
            if issimple(i)==[]:
                lst.append(i)
    return lst
r=issimple(48)
print(max(r))