# Реализуйте алгоритм,
# который принимает массив и перемещает нули в конец,
# сохраняя порядок остальных элементов 2 0 4 0 3 00

def algo(lst):
    lst = sorted(lst, reverse=True)
    return lst


print(algo([2, 3, 0, 3, 0, 2, 0, 1, 0]))

