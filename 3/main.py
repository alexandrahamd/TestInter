import json


class Operations:

    def __init__(self, data):
        self.__date = data.get('date')
        self.description = data.get('description')
        self.__where = data.get('from')
        self.__to = data.get('to')
        self.__summa = data.get('operationAmount')
        self.__currency = data.get('operationAmount')

    @property
    def to(self):
        if self.__to:
            a = self.__to.split()
            return f'{a[0]} **{a[1][:4]}'
        return 'нет информации'


    @to.setter
    def to(self, to):
        self.__to = to

    @property
    def where(self):
        if self.__where:
            a = self.__where.split()
            return f'{a[0]} {a[1][0:4]} {a[1][4:6]}** **** {a[1][12:]}'
        return 'нет информации'


    @where.setter
    def date(self, where):
        self.__where = where

    @property
    def date(self):
        if self.__date:
            return self.__date[:10]
        return 'нет информации'


    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def summa(self):
        a = self.__summa
        if a:
            return a.get('amount')
        else:
            return 'нет информации'


    @summa.setter
    def summa(self, summa):
        self.__summa = summa


    @property
    def currency(self):
        a = self.__summa
        if a:
            return a.get('currency').get('name')
        else:
            return 'нет информации'


    @currency.setter
    def currency(self, currency):
        self.__currency = currency

    def __repr__(self):
        return f'<{self.date}> <{self.description}>\n' \
               f'<{self.where}> --> <{self.to}>\n' \
               f'<{self.summa} {self.currency}>\n'


if __name__ == '__main__':
    with open('operations.json',  'r', encoding='utf-8') as f:
        text = json.load(f)
    all = [Operations(i) for i in text]
    all = sorted(all, key=lambda x: x.date, reverse=True)
    for class_item in range(5):
        print(all[class_item])

