import pygame
import screen as scrn_module

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (252, 252, 252)
COLOR_GREEN = (35, 142, 35)
COLOR_YELLOW = (252, 252, 0)
COLOR_ORANGE = (252, 165, 0)
COLOR_RED = (252, 0, 0)
COLOR_BLUE = (50, 153, 204)

BRICK_WIDTH = 720 / 14
BRICK_HEIGHT = 10

COLS = 14

GAP = 8


class Tile:
    def __init__(self, x, y, color, points, speed, surface, bounces):
        super().__init__()

        self.width = BRICK_WIDTH
        self.height = BRICK_HEIGHT
        self.x = x
        self.y = y
        self.color = color
        self.points = points
        self.speed = speed
        self.surface = surface
        self.rows = None
        self.bounces = bounces
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def drawBrick(self):
        pygame.draw.rect(self.surface, self.color, self.rect, width=0)


class Wall:
    def __init__(self, rows, columns, surface, x, y):
        super().__init__()
        self.tiles = []
        self.colors = []
        self.rows = rows
        self.columns = columns
        self.surface = surface
        self.x = x
        self.y = y
        self.create_wall()

    def create_wall(self):
        for i in range(self.rows):
            block_row = []
            for j in range(self.columns):
                brick_x = (j * (BRICK_WIDTH + GAP)) + self.x
                brick_y = (i * (BRICK_HEIGHT + GAP)) + self.y
                if i >= 0 and i < 2:
                    brick_color = COLOR_RED
                    brick_bounces = 1
                    brick_points = 7
                    brick_speed = 4
                elif i >= 2 and i < 4:
                    brick_color = COLOR_ORANGE
                    brick_bounces = 1
                    brick_points = 5
                    brick_speed = 3
                elif i >= 4 and i < 6:
                    brick_color = COLOR_GREEN
                    brick_bounces = 1
                    brick_points = 3
                    brick_speed = 2
                else:
                    brick_color = COLOR_YELLOW
                    brick_bounces = 1
                    brick_points = 1
                    brick_speed = 1
                brick_surface = self.surface

                block_row.append(
                    Tile(brick_x, brick_y, brick_color, brick_points, brick_speed, brick_surface, brick_bounces))

                # self.tiles.append(Tile(brick_x, brick_y, brick_color, brick_points, brick_speed, brick_surface))
            self.tiles.append(block_row)

    def draw(self):
        for tile in self.tiles:
            for brick in tile:
                brick.drawBrick()

    def redraw(self):
        self.tiles.clear()
        self.create_wall()
