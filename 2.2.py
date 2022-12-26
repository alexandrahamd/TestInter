# Посчитайте сумму н-го ряда пирамиды нечетных чисел (начало с 1)

def row_sum(n):
    row = []
    new = []

    if n > 1:
        for i in range(1, n*(n-1)):
            print(i)
            if i % 2 != 0:
                row.append(i)

        for i in range(row[-1]+2, row[-1]+(n*2)+2):
            if i % 2 != 0:
                new.append(i)
    else:
        return n

    return sum(new)


print(row_sum(4))


