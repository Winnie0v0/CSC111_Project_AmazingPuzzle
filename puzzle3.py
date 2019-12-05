from gameNumber import gameNumber
import pygame
pygame.init()


class puzzle3():
    """The 5*5 puzzle"""

    grid_len = 60
    square_len = grid_len * 3 // 5
    half_len = square_len // 2

    def __init__(self, color, x, y, win):
        """construct a square object;color is given as tuple (red, green, blue)
        """
        self.color = color
        self.win = win

        # x and y can be represented by GRID coordinates
        # from (1, 1) (1, 2)... to (5, 5)
        self.x = x
        self.y = y

    def draw(self):
        """create the pygame rectangle and draw the rectangle"""
        # (cor_x, cor_y) is the top-left corner of the square
        # convert GRID coordinates into GAME-WINDOW coordinates
        self.cor_x = 25 + (self.x-0.5)*puzzle3.grid_len - puzzle3.half_len
        self.cor_y = 25 + (self.y-0.5)*puzzle3.grid_len - puzzle3.half_len

        # create the rectangle and draw it
        self.sq = pygame.Rect(self.cor_x, self.cor_y, puzzle3.square_len, puzzle3.square_len)
        pygame.draw.rect(self.win, self.color, self.sq)

    def move_left(self):
        if self.x == 1 and self.y == 1:
            self.x = 1
            self.y = 1
        elif self.x == 1 and self.y == 2:
            self.x = 1
            self.y = 2
        elif self.x == 1 and self.y == 3:
            self.x = 3
            self.y = 1
        elif self.x == 1 and self.y == 4:
            self.x = 1
            self.y = 4
        elif self.x == 1 and self.y == 5:
            self.x = 1
            self.y = 5
        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 2
            self.y = 1
        elif self.x == 2 and self.y == 2:
            self.x = 2
            self.y = 2
        elif self.x == 2 and self.y == 3:
            self.x = 1
            self.y = 3
        elif self.x == 2 and self.y == 4:
            self.x = 2
            self.y = 4
        elif self.x == 2 and self.y == 5:
            self.x = 2
            self.y = 5
        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 3
            self.y = 1
        elif self.x == 3 and self.y == 2:
            self.x = 2
            self.y = 2
        elif self.x == 3 and self.y == 3:
            self.x = 2
            self.y = 3
        elif self.x == 3 and self.y == 4:
            self.x = 2
            self.y = 4
        elif self.x == 3 and self.y == 5:
            self.x = 2
            self.y = 5
        # x = 4
        elif self.x == 4 and self.y == 1:
            self.x = 3
            self.y = 1
        elif self.x == 4 and self.y == 2:
            self.x = 4
            self.y = 2
        elif self.x == 4 and self.y == 3:
            self.x = 3
            self.y = 3
        elif self.x == 4 and self.y == 4:
            self.x = 3
            self.y = 4
        elif self.x == 4 and self.y == 5:
            self.x = 3
            self.y = 5
        # x = 5
        elif self.x == 5 and self.y == 1:
            self.x = 4
            self.y = 1
        elif self.x == 5 and self.y == 2:
            self.x = 4
            self.y = 2
        elif self.x == 5 and self.y == 3:
            self.x = 4
            self.y = 3
        elif self.x == 5 and self.y == 4:
            self.x = 4
            self.y = 4
        elif self.x == 5 and self.y == 5:
            self.x = 5
            self.y = 5

    def move_right(self):
        # x = 1
        if self.x == 1 and self.y == 1:
            self.x = 1
            self.y = 1
        elif self.x == 1 and self.y == 2:
            self.x = 1
            self.y = 2
        elif self.x == 1 and self.y == 3:
            self.x = 2
            self.y = 3
        elif self.x == 1 and self.y == 4:
            self.x = 1
            self.y = 4
        elif self.x == 1 and self.y == 5:
            self.x = 1
            self.y = 5
        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 2
            self.y = 1
        elif self.x == 2 and self.y == 2:
            self.x = 3
            self.y = 2
        elif self.x == 2 and self.y == 3:
            self.x = 3
            self.y = 3
        elif self.x == 2 and self.y == 4:
            self.x = 3
            self.y = 4
        elif self.x == 2 and self.y == 5:
            self.x = 3
            self.y = 5
        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 4
            self.y = 1
        elif self.x == 3 and self.y == 2:
            self.x = 3
            self.y = 2
        elif self.x == 3 and self.y == 3:
            self.x = 4
            self.y = 3
        elif self.x == 3 and self.y == 4:
            self.x = 4
            self.y = 4
        elif self.x == 3 and self.y == 5:
            self.x = 4
            self.y = 5
        # x = 4
        elif self.x == 4 and self.y == 1:
            self.x = 5
            self.y = 1
        elif self.x == 4 and self.y == 2:
            self.x = 5
            self.y = 2
        elif self.x == 4 and self.y == 3:
            self.x = 5
            self.y = 3
        elif self.x == 4 and self.y == 4:
            self.x = 5
            self.y = 4
        elif self.x == 4 and self.y == 5:
            self.x = 4
            self.y = 5
        # x = 5
        elif self.x == 5 and self.y == 1:
            self.x = 5
            self.y = 3
        elif self.x == 5 and self.y == 2:
            self.x = 2
            self.y = 1
        elif self.x == 5 and self.y == 3:
            self.x = 5
            self.y = 1
        elif self.x == 5 and self.y == 4:
            self.x = 2
            self.y = 5
        elif self.x == 5 and self.y == 5:
            self.x = 5
            self.y = 5

    def move_up(self):
        # x = 1
        if self.x == 1 and self.y == 1:
            self.x = 5
            self.y = 5
        elif self.x == 1 and self.y == 2:
            self.x = 1
            self.y = 1
        elif self.x == 1 and self.y == 3:
            self.x = 1
            self.y = 2
        elif self.x == 1 and self.y == 4:
            self.x = 1
            self.y = 3
        elif self.x == 1 and self.y == 5:
            self.x = 1
            self.y = 4
        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 5
            self.y = 2
        elif self.x == 2 and self.y == 2:
            self.x = 2
            self.y = 1
        elif self.x == 2 and self.y == 3:
            self.x = 2
            self.y = 3
        elif self.x == 2 and self.y == 4:
            self.x = 2
            self.y = 4
        elif self.x == 2 and self.y == 5:
            self.x = 2
            self.y = 4
        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 1
            self.y = 3
        elif self.x == 3 and self.y == 2:
            self.x = 3
            self.y = 1
        elif self.x == 3 and self.y == 3:
            self.x = 3
            self.y = 3
        elif self.x == 3 and self.y == 4:
            self.x = 3
            self.y = 4
        elif self.x == 3 and self.y == 5:
            self.x = 3
            self.y = 5
        # x = 4
        elif self.x == 4 and self.y == 1:
            self.x = 4
            self.y = 1
        elif self.x == 4 and self.y == 2:
            self.x = 4
            self.y = 2
        elif self.x == 4 and self.y == 3:
            self.x = 4
            self.y = 2
        elif self.x == 4 and self.y == 4:
            self.x = 4
            self.y = 4
        elif self.x == 4 and self.y == 5:
            self.x = 4
            self.y = 5
        # x = 5
        elif self.x == 5 and self.y == 1:
            self.x = 5
            self.y = 1
        elif self.x == 5 and self.y == 2:
            self.x = 5
            self.y = 2
        elif self.x == 5 and self.y == 3:
            self.x = 5
            self.y = 3
        elif self.x == 5 and self.y == 4:
            self.x = 5
            self.y = 4
        elif self.x == 5 and self.y == 5:
            self.x = 5
            self.y = 4

    def move_down(self):
        # x = 1
        if self.x == 1 and self.y == 1:
            self.x = 1
            self.y = 2
        elif self.x == 1 and self.y == 2:
            self.x = 1
            self.y = 3
        elif self.x == 1 and self.y == 3:
            self.x = 1
            self.y = 4
        elif self.x == 1 and self.y == 4:
            self.x = 1
            self.y = 5
        elif self.x == 1 and self.y == 5:
            self.x = 4
            self.y = 5
        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 2
            self.y = 2
        elif self.x == 2 and self.y == 2:
            self.x = 2
            self.y = 2
        elif self.x == 2 and self.y == 3:
            self.x = 2
            self.y = 3
        elif self.x == 2 and self.y == 4:
            self.x = 2
            self.y = 5
        elif self.x == 2 and self.y == 5:
            self.x = 5
            self.y = 4
        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 3
            self.y = 2
        elif self.x == 3 and self.y == 2:
            self.x = 3
            self.y = 2
        elif self.x == 3 and self.y == 3:
            self.x = 3
            self.y = 3
        elif self.x == 3 and self.y == 4:
            self.x = 3
            self.y = 4
        elif self.x == 3 and self.y == 5:
            self.x = 3
            self.y = 5
        # x = 4
        elif self.x == 4 and self.y == 1:
            self.x = 4
            self.y = 1
        elif self.x == 4 and self.y == 2:
            self.x = 4
            self.y = 3
        elif self.x == 4 and self.y == 3:
            self.x = 4
            self.y = 3
        elif self.x == 4 and self.y == 4:
            self.x = 4
            self.y = 4
        elif self.x == 4 and self.y == 5:
            self.x = 4
            self.y = 5
        # x = 5
        elif self.x == 5 and self.y == 1:
            self.x = 5
            self.y = 1
        elif self.x == 5 and self.y == 2:
            self.x = 5
            self.y = 2
        elif self.x == 5 and self.y == 3:
            self.x = 5
            self.y = 3
        elif self.x == 5 and self.y == 4:
            self.x = 5
            self.y = 5
        elif self.x == 5 and self.y == 5:
            self.x = 1
            self.y = 1

    def coords(self):
        """return the tuple's coordinates"""
        return (self.x, self.y)


def main():

    # the game window has a dimension of 350*350
    # the grid takes up 300*300
    # the margin on each side is 50
    win = pygame.display.set_mode(size=(350, 350))
    pygame.display.set_caption("Amazing Puzzle - Level 999")

    # colors:
    grey = (60, 60, 60)  # color of the two "goals"
    white = (255, 255, 255)  # color of the numbers
    black = (0, 0, 0)  # background color
    red = (255, 0, 0)
    blue = (0, 0, 255)
    grid_color = (40, 60, 40)

    # the two moving squares
    sq1X = 1
    sq1Y = 2
    sq1 = puzzle3(red, sq1X, sq1Y, win)
    sq2X = 1
    sq2Y = 3
    sq2 = puzzle3(blue, sq2X, sq2Y, win)

    # the two "goals" of the game
    goal1 = puzzle3(grey, 1, 1, win)
    goal2 = puzzle3(grey, 3, 1, win)

    # the game loop!!!!!
    run = True
    crash = False  # crash when the two squares ovelap
    puzzlewin = False  # win when the grey squares are covered
    while run:

        for event in pygame.event.get():
            # Quit condition
            if event.type == pygame.QUIT:
                run = False

            # check if the user hits the arrow keys
            elif event.type == pygame.KEYDOWN:
                # left button hit
                if event.key == pygame.K_LEFT:
                    sq1.move_left()
                    sq2.move_left()
                # right button hit
                elif event.key == pygame.K_RIGHT:
                    sq1.move_right()
                    sq2.move_right()
                # up button hit
                elif event.key == pygame.K_UP:
                    sq1.move_up()
                    sq2.move_up()
                # down button hit
                elif event.key == pygame.K_DOWN:
                    sq1.move_down()
                    sq2.move_down()

        # check if the two squares ovelap in each loop
        if sq1.coords() == sq2.coords():
            run = False
            crash = True
        # check if the user wins in each loop
        elif (sq1.coords() == goal1.coords() and sq2.coords() == goal2.coords()) or\
             (sq1.coords() == goal2.coords() and sq2.coords() == goal1.coords()):
            run = False
            puzzlewin = True

        # refill the window to black in each loop
        win.fill(black)

        # draw everything:
        # background grid - vertical
        pygame.draw.line(win, grid_color, (25, 25), (25, 325), 3)
        pygame.draw.line(win, grid_color, (85, 25), (85, 325), 3)
        pygame.draw.line(win, grid_color, (145, 25), (145, 325), 3)
        pygame.draw.line(win, grid_color, (205, 25), (205, 325), 3)
        pygame.draw.line(win, grid_color, (265, 25), (265, 325), 3)
        pygame.draw.line(win, grid_color, (325, 25), (325, 325), 3)
        # background grid - horizontal
        pygame.draw.line(win, grid_color, (25, 25), (325, 25), 3)
        pygame.draw.line(win, grid_color, (25, 85), (325, 85), 3)
        pygame.draw.line(win, grid_color, (25, 145), (325, 145), 3)
        pygame.draw.line(win, grid_color, (25, 205), (325, 205), 3)
        pygame.draw.line(win, grid_color, (25, 265), (325, 265), 3)
        pygame.draw.line(win, grid_color, (25, 325), (325, 325), 3)

        # walls - vertical
        wall_ver_1 = pygame.image.load("wall_ver.jpg")
        wall_ver_1_rect = pygame.Rect(23, 23, 7, 126)
        win.blit(wall_ver_1, wall_ver_1_rect, wall_ver_1_rect)
        wall_ver_2 = pygame.image.load("wall_ver.jpg")
        wall_ver_2_rect = pygame.Rect(23, 203, 7, 126)
        win.blit(wall_ver_2, wall_ver_2_rect, wall_ver_2_rect)
        wall_ver_3 = pygame.image.load("wall_ver.jpg")
        wall_ver_3_rect = pygame.Rect(83, 23, 7, 126)
        win.blit(wall_ver_3, wall_ver_3_rect, wall_ver_3_rect)
        wall_ver_4 = pygame.image.load("wall_ver.jpg")
        wall_ver_4_rect = pygame.Rect(83, 203, 7, 126)
        win.blit(wall_ver_4, wall_ver_4_rect, wall_ver_4_rect)
        wall_ver_5 = pygame.image.load("wall_ver.jpg")
        wall_ver_5_rect = pygame.Rect(143, 23, 7, 66)
        win.blit(wall_ver_5, wall_ver_5_rect, wall_ver_5_rect)
        wall_ver_6 = pygame.image.load("wall_ver.jpg")
        wall_ver_6_rect = pygame.Rect(203, 83, 7, 66)
        win.blit(wall_ver_6, wall_ver_6_rect, wall_ver_6_rect)
        wall_ver_7 = pygame.image.load("wall_ver.jpg")
        wall_ver_7_rect = pygame.Rect(263, 263, 7, 66)
        win.blit(wall_ver_7, wall_ver_7_rect, wall_ver_7_rect)
        wall_ver_8 = pygame.image.load("wall_ver.jpg")
        wall_ver_8_rect = pygame.Rect(323, 263, 7, 66)
        win.blit(wall_ver_8, wall_ver_8_rect, wall_ver_8_rect)
        # walls - horizontal
        wall_hor_1 = pygame.image.load("wall_hor.jpg")
        wall_hor_1_rect = pygame.Rect(203, 23, 126, 7)
        win.blit(wall_hor_1, wall_hor_1_rect, wall_hor_1_rect)
        wall_hor_2 = pygame.image.load("wall_hor.jpg")
        wall_hor_2_rect = pygame.Rect(203, 83, 126, 7)
        win.blit(wall_hor_2, wall_hor_2_rect, wall_hor_2_rect)
        wall_hor_3 = pygame.image.load("wall_hor.jpg")
        wall_hor_3_rect = pygame.Rect(83, 143, 126, 7)
        win.blit(wall_hor_3, wall_hor_3_rect, wall_hor_3_rect)
        wall_hor_4 = pygame.image.load("wall_hor.jpg")
        wall_hor_4_rect = pygame.Rect(263, 143, 66, 7)
        win.blit(wall_hor_4, wall_hor_4_rect, wall_hor_4_rect)
        wall_hor_5 = pygame.image.load("wall_hor.jpg")
        wall_hor_5_rect = pygame.Rect(83, 203, 246, 7)
        win.blit(wall_hor_5, wall_hor_5_rect, wall_hor_5_rect)
        wall_hor_6 = pygame.image.load("wall_hor.jpg")
        wall_hor_6_rect = pygame.Rect(143, 263, 126, 7)
        win.blit(wall_hor_6, wall_hor_6_rect, wall_hor_6_rect)
        wall_hor_7 = pygame.image.load("wall_hor.jpg")
        wall_hor_7_rect = pygame.Rect(143, 323, 66, 7)
        win.blit(wall_hor_7, wall_hor_7_rect, wall_hor_7_rect)

        # draw the numbers
        size = 20
        game = 3
        n1_1 = gameNumber("1", size, white, (1, 3), "left", game)
        n1_1.draw(win)
        n1_2 = gameNumber("1", size, white, (3, 1), "up", game)
        n1_2.draw(win)
        n2_1 = gameNumber("2", size, white, (1, 5), "down", game)
        n2_1.draw(win)
        n2_2 = gameNumber("2", size, white, (4, 5), "down", game)
        n2_2.draw(win)
        n3_1 = gameNumber("3", size, white, (2, 5), "down", game)
        n3_1.draw(win)
        n3_2 = gameNumber("3", size, white, (5, 4), "right", game)
        n3_2.draw(win)
        n4_1 = gameNumber("4", size, white, (2, 1), "up", game)
        n4_1.draw(win)
        n4_2 = gameNumber("4", size, white, (5, 2), "right", game)
        n4_2.draw(win)
        n5_1 = gameNumber("5", size, white, (1, 1), "up", game)
        n5_1.draw(win)
        n5_2 = gameNumber("5", size, white, (5, 5), "down", game)
        n5_2.draw(win)
        n6_1 = gameNumber("6", size, white, (5, 1), "right", game)
        n6_1.draw(win)
        n6_2 = gameNumber("6", size, white, (5, 3), "right", game)
        n6_2.draw(win)

        # draw other things
        goal1.draw()
        goal2.draw()
        sq1.draw()
        sq2.draw()

        # update the display window in each loop
        pygame.display.update()

    # check if the two squares are on top of each other
    if crash:
        # display the "you lose you stupid" window
        pass

    # check is the user wins
    elif puzzlewin:
        # display the "you win" window
        pass

    pygame.quit()
    quit()


main()
