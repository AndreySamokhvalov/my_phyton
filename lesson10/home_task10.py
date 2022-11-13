from decorators import timer
from decorators import cacher
from decorators import logger
# from input_data import in_data
#from result      import save_result
import os
os.system("cls")
print('Добро пожаловать!')


@timer
@logger
@cacher
def function_from_n(n):
    out_list = []
    for i in range(0,n):
        out_list.append((1+i)**i)
    #print(out_list) 
    return out_list


function_from_n(800)
function_from_n(1000)
function_from_n(800)
function_from_n(2000)


# n = in_data() 


# def main():  
#     print('original:') 
#     function_from_n(n)
#     print('catch:')
#     function_from_n(n)


# main()
# save_result(function_from_n(n))
