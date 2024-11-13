'''Main executable file'''

import random as r

def func_1(args):
    '''Just a function'''
    print('=' * 60)
    return args[::-1]

def func_2(args):
    '''Just a function'''
    print('=' * 60)
    x = r.randint(0, len(args) - 1)
    args[x] = r.randint(0, 1000)
    return args

def func_3(*args):
    '''Just a function'''
    print('=' * 60)
    i = 1
    while i < len(args):
        x1 = args[i]
        x2 = args[i-1]
        if x1 == x2:
        #if args[i] == args[i-1]:
            i += 1
        else:
            return False
    return True

def func_4(args, start = 0, end = 10, step = 1):
    '''Just a function'''
    print('=' * 60)
    end = len(args)
    return args[start:end:step]

def func_5(create, amount = 4, random_fill = True, add = False, fill_range = None):
    '''Just a function'''
    print('=' * 60)
    if fill_range is None:
        fill_range = [0, 10]
    if not create:  # if the list has been passed it will not trigger
        x = []
        if random_fill:
            while len(x) < amount:
                x.append(r.randint(0, 1000))
        else:
            i = fill_range[0]
            while len(x) < fill_range[1] - 1:
                x.append(i)
                i += 1
    else:           # Triggered only when the lisy is not passed
        x = create  # Takes in a list
        amount = len(x) + amount
        if add:
            if random_fill:
                while len(x) < amount:
                    x.append(r.randint(0, 1000))
            else:
                i = fill_range[0]
                while len(x) < fill_range[1] - 1:
                    x.append(i)
                    i += 1
        else:
            x.clear()
            if random_fill:
                while len(x) < amount:
                    x.append(r.randint(0, 1000))
            else:
                element = fill_range[0]
                while len(x) < fill_range[1] - 1:
                    x.append(element)
                    element += 1
    return x

def func_6(args, slot = 0):
    '''Just a function'''
    print('=' * 60)
    x = slot
    if x > len(args) or x < 0:
        print('Selected index was out of range')
        print('Random index will be selected')
        x = r.randint(0, len(args) - 1)
    args[x] = r.randint(0, 1000)
    return args

def func_7(*args, sort_descending = False):
    '''Just a function'''
    print('=' * 60)
    i = 1
    x = args[0] # Making it the main list
    while i < len(args):
        for y in args[i]:
            x.append(y)
        i += 1
    x.sort(reverse=sort_descending)
    return x

def func_8():
    '''Just a function'''
    print('=' * 60)

    def create_list():
        '''Sub function made to create list'''
        length = r.randint(1, 50)    # Length of the list
        i = 0
        xs = []
        while i < length:
            xs.append(r.randint(1, 20))
            i += 1
        return xs

    x = create_list()
    while len(x) % 2 == 0:
        x = create_list()
    mid = len(x) // 2
    mid = x[mid]
    i = x.count(mid)
    return i, mid, x

def func_9(*args, size = 15):
    '''Just a function'''
    print('=' * 60)
    x = []
    for i in args:
        x += i
    while len(x) > size:
        x.pop()
    x.sort()
    return x
# Needs to be done ASAP
def func_10():
    '''Just a function'''
    print('=' * 60)
    def funct_1():
        '''Just a function'''
        print('=' * 60)
    def funct_2():
        '''Just a function'''
        print('=' * 60)
    def funct_3():
        '''Just a function'''
        print('=' * 60)
    def funct_4():
        '''Just a function'''
        print('=' * 60)
    def funct_5():
        '''Just a function'''
        print('=' * 60)
    def funct_6():
        '''Just a function'''
        print('=' * 60)
    funct_1()
    funct_2()
    funct_3()
    funct_4()
    funct_5()
    funct_6()

def func_11(args):
    '''Just a function'''
    print('=' * 60)
    return args.pop(args.index(min(args))) , args

def func_12(*args):
    '''Just a function'''
    print('=' * 60)
    return list(map(lambda x: x * x, args))

def func_13(*args):
    '''Just a function'''
    print('=' * 60)
    return list(map(lambda x: type(x), args))

def func_14(*args, elem):
    '''Just a function'''
    print('=' * 60)
    if args.count(elem) != 0 and args.count(elem) > 0:
        return True
    return False

def func_15(*args):
    '''Just a function'''
    print('=' * 60)
    return list(map(lambda x: x, args))

def func_16(*args):
    '''Just a function'''
    print('=' * 60)
    def do_1(dicto):
        '''Get random data from dictionary'''
        x = list(map(lambda x: x, dicto.keys()))
        y = x[r.randint(0, len(x) - 1)]
        return f'{y} : {dicto.get(y)}'
    def do_2(dicto):
        '''Sort func'''
        xy = []
        x = list(map(lambda x: x, dicto))
        x.sort()
        for i in x:
            vals = list()
            s = dicto.get(i)
            vals.append(i)
            vals.append(s)
            xy += vals
        return xy
    def do_3(dicto):
        '''Sort by value'''
        return sorted(dicto.items(), key=lambda x: x[1])

    return do_1(args[0]), do_2(args[1]), do_3(args[2])


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
