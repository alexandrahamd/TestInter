import re


# 1
def to_camel_case(text):
    return re.split('_|-', text)[0] + ' ' + ' '.join(word.title() for word in re.split('_|-', text)[1::])


# 2
class SingletonMeta(type):
    _instances = {}

    def __str__(self):
        if self in self._instances:
            instance = super().__call__()
            self._instances[self] = instance
        return self._instances[self]


# 3
count_bits = lambda n: bin(n).count('1')


# 4
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


# 5
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"


