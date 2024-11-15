'''Sub file made to contain code'''

# pylint:disable=W0108

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
def func_10(args):
    '''Just a function'''
    print('=' * 60)
    def funct_1(a):
        '''Just a function'''
        print(sorted(list(map(lambda x: x % 2, a)), reverse = True))
        print(a)
        print('*' * 60)
    def funct_2(a):
        '''Just a function'''
        y = list(filter(lambda z: z % 2 == 0, list(map(lambda x: x * x, a))))
        print(a)
        print(y)
        print('*' * 60)
    def funct_3(a):
        '''Just a function'''
        x = sorted(list(map(int, list(map(lambda y: y[2:],
            list(map(lambda x: bin(x), a)))))), reverse=True)
        print(x)
        print('*' * 60)
    def funct_4(a):
        '''Just a function'''
        x = sorted(a, key=lambda x: (x ** 2) // 2)
        print(x)
        print('*' * 60)
    def funct_5(a):
        '''Just a function'''
        x = list(filter(lambda x: x > 0, a))
        print(x)
        print('*' * 60)
    def funct_6(a):
        '''Just a function'''
        x = list(filter(lambda x: x < 0, a))
        print(x)
    funct_1(args)
    funct_2(args)
    funct_3(args)
    funct_4([123, 34, 1, 6, 76, 0, 23, 4, 3, 12, 3])
    funct_5([-1, 2, -10, -2, 12, 13, -4, 6])
    funct_6([-1, 2, -10, -2, 12, 13, -4, 6])
    return 'Function block finished execution'

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

def func_17(*args, key):
    '''Just a function'''
    print('=' * 60)
    y = list()
    x = list(map(lambda x: list(map(lambda x: x, x)), args))
    for i in x:
        y += i
    return y.count(key), y

def func_18(args, element):
    '''Just a function'''
    print('=' * 60)
    xy = list()
    for x in args:
        print(x)
        for y in args[x]:
            print(y)
            for k in args[x][y]:
                if k == element:
                    xy.append(args[x][y].get(element, None))
    return xy
