'''Main executable file'''

# pylint:disable=W0401, W0614

from task import *



if __name__ == '__main__':
    this = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    that = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
    those =[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    capitals = {
    'Russia': 'Moscow',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Japan': 'Tokyo'
    }

    currency_rates = {
    'USD': 60,
    'EUR': 65,
    'GBP': 70,
    'JPY': 80,
    'CHF': 90
    }

    prices = {
    'Bread': 40,
    'Milk': 35,
    'Cheese': 45,
    'Butter': 55,
    'Yogurt': 20
    }

    dict_1 = {
        '1' : 'Evan',
        '2' : 'Sun',
        '3' : 'Kiylith',
        '4' : 'Robert',
        '5' : 'Johana'
    }

    dict_2 = {
        '1' : 'Bob',
        '2' : 'Tanya',
        '3' : 'Milly',
        '4' : 'Anna',
        '5' : 'Kate'
    }

    dict_3 = {'1': 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5}

    print(func_1(this))
    print(func_2([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    print(func_3(this, that, those))
    print(func_4(that, start=3, end=7, step=2))
    print(func_5(that, 7, True, True, [2, 22]))
    print(func_6(those, 6))
    print(func_7(that, those, sort_descending=False))
    print(func_8())
    print(func_9(this, that, size= 15))

    print(func_11(this))
    print(func_12(1, 2, 3, 4, 5, 6))
    print(func_13(1, '1', 3.02, 'Text', 5, 6))
    print(func_14(1, 2, 3, 4, 5, 6, elem=6))
    print(func_15(this, that, this))
    print(func_16(capitals, currency_rates, prices))
    print(func_17(dict_1, dict_2, dict_3, key='3'))
