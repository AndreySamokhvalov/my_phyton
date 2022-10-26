# деление 
def division(a, b):
    return a/b

# случайная функция 1
def funk_one(num):
    sum_res = 0
    for i in range(1, num+1):
        res = round(3*i+1)
        sum_res += res
    sum_res = round(sum_res, 2)
    return sum_res

# квадратный корень
def sqrt(x):
    return x**(1/2)

# случайная функция 2
def funk_two(y):
    sum_res = 0
    for i in range(1, y):
        res = round(i**3-2, 18)
        sum_res += res
    sum_res = round(sum_res, 2)
    return sum_res-y

# натуральность
def check_simple(simple_num):
    for i in range(2, (simple_num//2+1)):
        if (simple_num % i == 0):
            return False
    return True

# поиск максимаоьного элемента списка
def find_max_index(list):
    i = 0 
    maxa=list[0]
    while i < len(list):
        if list[i]>maxa:
            maxa=list[i]
        i+=1
    return maxa


# перевод в двоичную систему
def number_conversion(input_namber):
    binary = ''
    while input_namber > 0:
      binary = str(input_namber % 2) + binary
      input_namber = input_namber // 2
    return binary
