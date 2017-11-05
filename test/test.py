from app import mayaprototypetool


def this_func(mult=0):
    a = 1
    b = 1
    if (a - b) == 2:
        raise Exception('No way')
    return (a + b) * mult


def haha():
    a = 1
    n = 3
    c = 5
    print(a, n)


print('The result is {0} and {1}'.format(this_func(20), mayaprototypetool.run_this()))
