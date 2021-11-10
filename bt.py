import pygame

pygame.init()


class Button:
    def __init__(self, img, x, y, value=999):
        """
        :param img: image of the button
        :param x: x coordinate in window
        :param y: y coordinate in window
        :param value: numerical or operational value of the button (0-9, mathematical op , = , clear)
        """
        self.img = img
        self.x = x
        self.y = y
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.value = value

    def draw(self, screen):
        """
        draw the button on the screen
        :param screen: the created pygame window
        :return:
        """
        screen.blit(self.img, (self.x, self.y))

    # print(self.rect)

    def check_col(self):
        """
        checks if left mouse clicked the button
        :return:
        """
        # get mouse position
        pos = pygame.mouse.get_pos()
        action = False

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                print("clicked")
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
