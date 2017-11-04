def test_this_func():
    print('This is running and expecting a raise Exception')
    a = 1
    b = 1
    if (a + b) > 2:
        raise Exception('haha this fails')

var = 5
for i in range(var):
    print(i)

print('whaaat?')

test_this_func()
