

def this_func(mult=0):
    a = 1
    b = 1
    if (a - b) == 2:
        raise Exception('No way')
    return (a + b) * mult


print('The result is {0} and'.format(this_func(20)))
