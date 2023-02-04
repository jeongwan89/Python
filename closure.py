def outer_func(tag):  # 1
    text = 'Some text'  # 5
    tag = tag  #6

    def inner_func():  # 7
        print('<{0}>{1}<{0}>'.format(tag, text))  # 9

    return inner_func  # 8

h1_func = outer_func('h1')  # 2
p_func = outer_func('p')  # 3

h1_func()  # 4
p_func()  # 10