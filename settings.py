# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = int(582 * 1.5)
HEIGHT = int(582 * 1.5)  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 200
TITLE = "Automate Maze Solver"
BGCOLOR = DARKGREY

TILESIZE = 9
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# player settings
PLAYER_MOVE_DELAY = 1