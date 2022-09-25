#Найти расстояние между двумя точками пространства.
import os
os.system("cls")
print('Добро пожаловать!')


A = input("Введите координаты точки A в формате Х Y Z через пробел : ")
A_list= A.split(sep=' ')


B = input("Введите координаты точки B в формате Х Y Z через пробел : ")
B_list= B.split(sep=' ')

#Расчет евклидова расстояния
distance = ((float(A_list[0])-float(B_list[0]))**2+(float(A_list[1])-float(B_list[1]))**2+(float(A_list[2])-float(B_list[2]))**2)**(0.5)

print(f'Расстояние между точкой A({A_list[0]},{A_list[1]},{A_list[2]}) и точкой B({B_list[0]},{B_list[1]},{B_list[2]}) равно {distance}')


