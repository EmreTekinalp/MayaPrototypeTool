from src import mayaprototypetool

def test_this_func(mult):
    a = 1
    b = 1
    return (a + b) * mult


print('The result is {0} and {1}'.format(test_this_func(20), mayaprototypetool.run_this()))
