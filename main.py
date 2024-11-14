'''Main executable file'''

# pylint:disable=W0401, W0614

from task import *
from dictionaries import *

if __name__ == '__main__':
    this = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    that = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
    those =[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


    print(func_1(this))
    print(func_2([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    print(func_3(this, that, those))
    print(func_4(that, start=3, end=7, step=2))
    print(func_5(that, 7, True, True, [2, 22]))
    print(func_6(those, 6))
    print(func_7(that, those, sort_descending=False))
    print(func_8())
    print(func_9(this, that, size= 15))
    print(func_10(those))
    print(func_11(this))
    print(func_12(1, 2, 3, 4, 5, 6))
    print(func_13(1, '1', 3.02, 'Text', 5, 6))
    print(func_14(1, 2, 3, 4, 5, 6, elem=6))
    print(func_15(this, that, those))
    print(func_16(capitals, currency_rates, prices))
    print(func_17(dict_1, dict_2, dict_3, key='3'))
    print(func_18(dict_huge, 'id'))
