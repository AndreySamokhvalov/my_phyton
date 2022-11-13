import time
import datetime
from functools import wraps
import os
os.system("cls")

#таймер
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        finish = time.time()
        total = finish - start
        print (f'время работы: {total} ')
        return res
    return wrapper


#кеширование
def cacher(func):
    cath = {}
    def wrapper(*args):
        res = func(*args)
        key = args
        if key not in cath:
            cath[key] = func(*args)
        # print(cath)
        return cath[key]
    return wrapper


#логирование
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        log_msg += f'Функция: function_from_n(n)\t'
        log_msg += f"Значение n: {*args, *kwargs}\t"
        start = time.time()
        res = func(*args, **kwargs)
        finish = time.time()
        total = finish - start
        log_msg += f"Время работы: {total}\n"
        res = func(*args, **kwargs)
        with open('log_file.log', 'a', encoding='utf-8') as file:
            file.write(log_msg)
        return res
    return wrapper

