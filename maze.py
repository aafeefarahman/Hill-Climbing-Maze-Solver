import pygame
import sys
import random

# --------------------
# CONFIG
# --------------------
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 20, 20
CELL_SIZE = WIDTH // COLS

# COLORS
BACKGROUND = (240, 248, 255)
WALL = (120, 50, 180)
GRID = (200, 200, 200)
AGENT = (255, 80, 80)
GOAL = (80, 200, 120)
PATH = (100, 180, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hill Climbing Maze Solver")
clock = pygame.time.Clock()

start = (0, 0)
goal = (ROWS - 1, COLS - 1)

# --------------------
# RESET MAZE
# --------------------
def reset_maze():
    global maze, agent_pos, stuck, path

    maze = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < 0.25:
                maze[i][j] = 1

    maze[start[0]][start[1]] = 0
    maze[goal[0]][goal[1]] = 0

    agent_pos = start
    stuck = False
    path = []

reset_maze()

# --------------------
# HEURISTIC
# --------------------
def heuristic(pos):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

# --------------------
# NEIGHBORS
# --------------------
def get_neighbors(pos):
    neighbors = []
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    for d in directions:
        r = pos[0] + d[0]
        c = pos[1] + d[1]

        if 0 <= r < ROWS and 0 <= c < COLS:
            if maze[r][c] == 0:
                neighbors.append((r,c))

    return neighbors

# --------------------
# HILL CLIMB
# --------------------
def hill_climb(current):
    neighbors = get_neighbors(current)
    if not neighbors:
        return current

    best = current
    best_h = heuristic(current)

    for n in neighbors:
        h = heuristic(n)
        if h < best_h:
            best = n
            best_h = h

    return best

# --------------------
# DRAW
# --------------------
def draw():

    screen.fill(BACKGROUND)

    for r in range(ROWS):
        for c in range(COLS):

            rect = pygame.Rect(c*CELL_SIZE,r*CELL_SIZE,CELL_SIZE,CELL_SIZE)

            if maze[r][c] == 1:
                pygame.draw.rect(screen,WALL,rect)
            else:
                pygame.draw.rect(screen,GRID,rect,1)

    # draw visited path
    for p in path:
        pygame.draw.rect(
            screen,
            PATH,
            (p[1]*CELL_SIZE,p[0]*CELL_SIZE,CELL_SIZE,CELL_SIZE)
        )

    # draw goal
    pygame.draw.rect(
        screen,
        GOAL,
        (goal[1]*CELL_SIZE,goal[0]*CELL_SIZE,CELL_SIZE,CELL_SIZE)
    )

    # draw agent
    pygame.draw.rect(
        screen,
        AGENT,
        (agent_pos[1]*CELL_SIZE,agent_pos[0]*CELL_SIZE,CELL_SIZE,CELL_SIZE)
    )

    pygame.display.update()

# --------------------
# MAIN LOOP
# --------------------
running = True

while running:

    clock.tick(5)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_maze()

    if agent_pos != goal and not stuck:

        next_pos = hill_climb(agent_pos)

        if next_pos == agent_pos:
            print("Local maxima reached!")
            stuck = True
        else:
            path.append(agent_pos)
            agent_pos = next_pos

    draw()

pygame.quit()
sys.exit()