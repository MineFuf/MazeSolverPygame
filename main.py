import pygame as pg
import sys
from settings import *
from sprites import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(100, 500)
        self.load_data()

    def load_data(self):
        pass

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        lines = ['################', '#..............#',
                 '#.P............#', '#..............#',
                 '#..............#', '#..............#',
                 '#..............#', '#..............#',
                 '#..............#', '#..............#',
                 '#..............#', '#..............#',
                 '#..............#', '#...........E..#',
                 '#..............#', '################']
        for idx, line in enumerate(lines):
            for idy, tile in enumerate(line):
                if tile == '#':
                    Wall(self, idx, idy)
                elif tile == 'P':
                    self.player = Player(self, idx, idy)
                elif tile == 'E':
                    self.exit = vec(idx, idy)

        '''
        walls = []

        for i in range(int(WIDTH / TILESIZE)):
            walls.append((i, 0))
            walls.append((i, HEIGHT / TILESIZE - 1))
        for i in range(1, int(WIDTH / TILESIZE) - 1):
            walls.append((0, i))
            walls.append((HEIGHT / TILESIZE - 1, i))

        add_walls(self, walls)
        is_found_free = False
        for i in range(int(WIDTH / TILESIZE)):
            for j in range(int(HEIGHT / TILESIZE)):
                if not is_found_free:
                    is_this_free = True
                    for wall in walls:
                        if wall[0] == i and wall[1] == j:
                            is_this_free = False
                    if is_this_free:
                        self.player = Player(self, i, j)
                        print('Created player at ' + str((i, j)))
                        is_found_free = True
        '''

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()