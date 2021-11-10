import pygame
import bt
# initialize the pygame library
pygame.init()

font = pygame.font.Font('imgs/digital-7.ttf', 18)
BG_COLOR = (66, 135, 245)

# create the screen
screen = pygame.display.set_mode((350, 500))
pygame.display.set_caption('Calculator')
icon = pygame.image.load('imgs/calculator.png')
pygame.display.set_icon(icon)

# load images
display = bt.Button(pygame.image.load('imgs/display.png'), 20, 20)

b7 = bt.Button(pygame.image.load('imgs/7.png'), 20, 120, 7)
b8 = bt.Button(pygame.image.load('imgs/8.png'), 100, 120, 8)
b9 = bt.Button(pygame.image.load('imgs/9.png'), 180, 120, 9)
b_div = bt.Button(pygame.image.load('imgs/div.png'), 280, 120, '/')

b4 = bt.Button(pygame.image.load('imgs/4.png'), 20, 200, 4)
b5 = bt.Button(pygame.image.load('imgs/5.png'), 100, 200, 5)
b6 = bt.Button(pygame.image.load('imgs/6.png'), 180, 200, 6)
b_minus = bt.Button(pygame.image.load('imgs/minus.png'), 280, 200, '-')

b1 = bt.Button(pygame.image.load('imgs/1.png'), 20, 280, 1)
b2 = bt.Button(pygame.image.load('imgs/2.png'), 100, 280, 2)
b3 = bt.Button(pygame.image.load('imgs/3.png'), 180, 280, 3)
b_plus = bt.Button(pygame.image.load('imgs/plus.png'), 280, 280, '+') #added '+' check for bugs and interaction that assume it is integer value

c = bt.Button(pygame.image.load('imgs/c.png'), 20, 360, 'c')
b0 = bt.Button(pygame.image.load('imgs/0.png'), 100, 360, 0)
b_equal = bt.Button(pygame.image.load('imgs/equal.png'), 180, 360, '=')
b_multi = bt.Button(pygame.image.load('imgs/multi.png'), 280, 360, '*')

# button list
b_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b0, b_multi, b_plus, b_minus, b_div, b_equal, c]
num_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b0]

calc_line = ''




running = True
ans = ''
equal_pressed = False

# draw background
screen.fill(BG_COLOR)

# draw all buttons in their assigned locations
for button in b_list:
    button.draw(screen)

while running:

    # draw calculator display
    display.draw(screen)

    if calc_line != '':
        # displays the expression to be calculated and the answer once it has been calculated
        # display location (mid left of display)
        screen.blit(font.render(calc_line, True, (0, 0, 0)), (30, 40))
    if ans != '' and equal_pressed:
        # displays the answer (calculated expression)
        # display location - bottom right
        screen.blit(font.render(ans, True, (0, 0, 0)), (250 - 10*len(ans), 70)) # moves the location as the digits in the answer increase

    for button in b_list:
        if button.check_col():
            # checks for all buttons if the were pressed
            if type(button.value) == int:
                # if the button is a number add it to calc_line
                if equal_pressed == False:
                    if len(calc_line) < 25:
                        calc_line = f'{calc_line}{button.value}'
                else:
                    # if the calc_line is displaying a result of the previous expression replace the result with the new number
                    calc_line = f'{button.value}'
                    equal_pressed = False
            if button.value in ['+', '/', '-', '*'] :
                # if the button is an operation add it to the expression
                if len(calc_line) < 25:
                    calc_line = f'{calc_line}{button.value}'
                    equal_pressed = False
            if button.value == '=':
                # if the button is = calculate the calc_line expression adn place it in calc_line
                # if the user clicked on '=' with an uncomplete expression do not calculate
                try:
                    calc_line = f'{eval(calc_line)}'
                    equal_pressed = True
                    ans = calc_line
                except SyntaxError:
                    screen.blit(font.render('error', True, (0, 0, 0)), (30, 50))
                    pass
            if button.value == 'c':
                calc_line = ''
                ans = ''
            print(calc_line)

    # exit loop for pygame window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
