from pygame import *
import os

init()

a1 = False
a2 = False

size = (800, 600)

screen = display.set_mode(size)

ARIAL_50 = font.SysFont('arial', 50)

#Функция рестарта при прожатии соответствующей кнопки в окне
def startgame():
    os.startfile('Need For Vkid.py')

#Функция возврата к стратовому меню
def retitle():
    os.startfile('title.py')

#Функция, необходимая для того, чтобы при прожатии "Начать заново" игра началась заново
def rea1():
    global a1
    a1 = True
    return a1

#Функция, необходимая для того, чтобы при прожатии "Вернуться в меню" программа вернулась к начальному меню
def rea2():
    global a2
    a2 = True
    return a2

#Введение класса меню (добвление в него опций таких как начать игру и т.д.)
class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._option_surfaces.append(ARIAL_50.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i , option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)
#Сами опции меню и команды, которые выполняют при их прожатии
menu = Menu()
menu.append_option('Game Over!', lambda: print(''))
menu.append_option('Начать заново', rea1)
menu.append_option('Вернуться в меню', rea2)
menu.append_option('Выход из игры', quit)

#Цикл работы программы
running = True
while running:
    if a1:
        startgame()
        quit()
    if a2:
        retitle()
        quit()
    #Реакция программы на нажатия клавишь
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                menu.switch(-1)
            elif e.key == K_s:
                menu.switch(1)
            elif e.key == K_SPACE:
                menu.select()

    screen.fill((0, 0, 0))

    menu.draw(screen, 100, 100, 75)

    display.flip()
quit()