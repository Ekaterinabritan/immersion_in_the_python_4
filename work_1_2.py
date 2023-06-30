# Задание №1
# Напишите функцию для транспонирования матрицы
# Пример:
# [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def transpose(nums: list[int]) -> list [int]:
    return list(map(list, zip(*nums)))


print(transpose([[1, 2, 3], [4, 5, 6]]))


#Задание№2
# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента.
# (речь идет про **kwargs)
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("Значение для {} является {}".format(key, value))


print_values(
    name_1="one",
    name_2="two",
    name_3="three",
    name_4="four",
    name_5="five"
)