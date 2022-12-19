from title import Menu


def change_a():
    global a
    a += 1
    return a

def _change_a():
    global a
    a += 2
    return a


def test_select():
    global a
    menu.select()
    assert a == 1

def test_switch():
    global a
    menu.switch(1)
    menu.select()
    assert a == 3


a = 0
menu = Menu()
menu.append_option("", change_a)
menu.append_option("", _change_a)