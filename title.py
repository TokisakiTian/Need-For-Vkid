from pygame import *
import os

init()

a = False

size = (800, 600)

screen = display.set_mode(size)

ARIAL_50 = font.SysFont('arial', 50)

def startgame():
    """

    :return: has no return
    """
    os.startfile('Need For Vkid.py')

def rea():
    """
    :return: changes False to True in parameter a
    """
    global a
    a = True
    return a

class Menu:
    def __init__(self):
        """

        """
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        """
        adds options to the menu
        :param option: current option in the menu
        :param callback: task that current option completes
        :return: has no return
        """
        self._option_surfaces.append(ARIAL_50.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        """

        :param direction: changes of current index
        :return: has no return
        """
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        """

        :return: has no return
        """
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        """

        :param surf: not painted frame of option
        :param x: coordinate x of surf
        :param y: coordinate y of surf
        :param option_y_padding: height of surf
        :return: has no return
        """
        for i , option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)

if __name__ == '__main__':
    menu = Menu()
    menu.append_option('Need For Vkid', lambda: print(''))
    menu.append_option('???????????? ????????', rea)
    menu.append_option('?????????? ???? ????????', quit)
    running = True
    while running:
        if a:
            startgame()
            quit()
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
