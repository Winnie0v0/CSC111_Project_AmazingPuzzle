import pygame
pygame.init()


class gameNumber():
    """for creating numbers around the game board"""

    def_font = "arial"  # the default font of this class

    def __init__(self, text, size, color, pos, direction, puzzle):
        """create a BOLD but NOT ITALIC text object; text is a string;
        size is an integer; color is a tuple (r, g, b);
        pos is a tuple (x, y) -- the position of the box that the number is next to;
        direction is string -- must be 'left', 'right', 'up', or 'down';
        puzzle is integer -- must be 1, 2, or 3
        """
        self.text = text
        self.size = size
        self.color = color
        self.pos = pos

        # the coordinates of the grid next to the number
        x = self.pos[0]
        y = self.pos[1]

        # to check the puzzle you are creating numbers for
        # create numbers for puzzle 1
        if puzzle == 1:
            grid_len = 200
            if direction == 'left':
                x2 = 25
                y2 = 50 + (y-0.5)*grid_len
            elif direction == 'right':
                x2 = 665
                y2 = 50 + (y-0.5)*grid_len
            elif direction == 'up':
                x2 = 50 + (x-0.5)*grid_len
                y2 = 10
            elif direction == 'down':
                x2 = 50 + (x-0.5)*grid_len
                y2 = 655

        # create numbers for puzzle 2
        elif puzzle == 2:
            grid_len = 150
            if direction == 'left':
                x2 = 25
                y2 = 50 + (y-0.5)*grid_len
            elif direction == 'right':
                x2 = 665
                y2 = 50 + (y-0.5)*grid_len
            elif direction == 'up':
                x2 = 50 + (x-0.5)*grid_len
                y2 = 10
            elif direction == 'down':
                x2 = 50 + (x-0.5)*grid_len
                y2 = 655

        # create numbers for puzzle 3
        elif puzzle == 3:
            grid_len = 120
            # if the number is at the left side of the grid
            if direction == "left":
                x2 = 16
                y2 = 50 + (y-0.5)*grid_len - 20
            # if the number is at the right side of the grid
            elif direction == "right":
                x2 = 664
                y2 = 50 + (y-0.5)*grid_len - 20
            # if the number is above the grid
            elif direction == "up":
                x2 = 50 + (x-0.5)*grid_len - 4
                y2 = 6
            # if the number is at the bottom of the grid
            elif direction == "down":
                x2 = 50 + (x-0.5)*grid_len - 4
                y2 = 652

        self.coords = (x2, y2)
        # create the text surface and render it
        fon = pygame.font.SysFont(gameNumber.def_font, self.size, True, False)
        self.sur = fon.render(self.text, True, self.color)

    def draw(self, win):
        """draw text on a certain window"""
        win.blit(self.sur, self.coords)
