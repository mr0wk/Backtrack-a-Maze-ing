import pygame
import random

# Initialize pygame.
pygame.init()

# Create the screen.
screen = pygame.display.set_mode((800, 600))

# Title
pygame.display.set_caption("Raze Munner")

# PARAMETERS

# z is a base number for rectangular x value.
z = 30

# Cell's width and height:
x = z
y = z

line_w = 2

# No. of vertical and horizontal lines of the grid.
lines_n = 10
vertical = lines_n
horizontal = lines_n

# Maze's width and height.
maze_width = (lines_n - 1) * z + line_w
maze_height = maze_width
maze_z = maze_width

# No. of all cells.
cells_n_in_row = lines_n - 1
all_cells_n = cells_n_in_row ** 2

# Visited cells.
visited_cells = []

# Way the algorithm got to the specific cells.
all_cell_into = {}


# Grid
def create_grid():
    global x, y
    for n in range(vertical):
        pygame.draw.line(surface=screen,
                         color=(255, 255, 255),
                         start_pos=(x, y),
                         end_pos=(x, vertical * z),
                         width=line_w
                         )
        x += z
    x = z
    for n in range(horizontal):
        pygame.draw.line(surface=screen,
                         color=(255, 255, 255),
                         start_pos=(x, y),
                         end_pos=(horizontal * z, y),
                         width=line_w
                         )
        y += z
    y = z

# These two functions below at it's core were meant to generate two random points on the grid, the starting point and
# the endpoint of the maze and indicate them by drawing two rectangles: green and red. They still do that but the
# rectangles are now dark so you can't see them cause the idea was withdrawn but these functions play role in creating
# the maze so I didn't discard them.


def create_starting_point(color):
    on_x_axis = random.randint(0, 1)
    possible_cords = []
    for i in range(cells_n_in_row):
        possible_cords.append(0 + (i + 1) * z)
    if on_x_axis == 0:
        cords = (0, random.choice(possible_cords))
    else:
        cords = (random.choice(possible_cords), 0)

    point = pygame.draw.rect(surface=screen,
                             color=color,
                             rect=(cords[0] + line_w,
                                   cords[1] + line_w,
                                   x - line_w,
                                   y - line_w
                                   )
                             )
    return point


def create_points():
    starting_point = create_starting_point(color=(0, 0, 0))
    endpoint = create_starting_point(color=(0, 0, 0))
    if endpoint == starting_point:
        create_points()
    else:
        return [starting_point, endpoint]


def create_maze():
    global maze_block_x_cord, maze_block_y_cord

    def check_possible_directions_and_go(destination):
        # Checks if chosen destination is out of maze's width or height.

        # Left or up out of range.
        if destination < z + line_w:
            destination += z
            return destination
        # Right or down out of range.
        elif destination > maze_z:
            destination -= z
            return destination
        else:
            return destination

    # Randomly pick whether to check and go up or down or sideways.
    # Choose the axis for the movement.
    axis = random.choice(["x", "y"])

    # The direction differs depending on the axis. "x" is left or right, "y" is up or down.
    direction = random.choice([z, -z])

    if axis == "x":
        maze_block_x_cord = check_possible_directions_and_go(destination=maze_block_x_cord + direction)
        # These params indicate the cell which the algorithm went to.
        current_cell = (maze_block_x_cord, maze_block_y_cord)

        if current_cell[0] != maze_width and direction == -z:
            # If we're moving left or if our x cords are not on the first possible x value delete the wall on the
            # left. The algorithm can't delete the wall on the left while being in the first column because we would
            # end up with borderless maze on the left side, same thing for other borders.

            if current_cell not in visited_cells:
                # If the algorithm did not visit current cell we can save the information about by going which way did
                # he reach this cell and allow it to delete the wall.

                if current_cell not in all_cell_into:
                    all_cell_into[current_cell] = "Left"

                # The illusion of deleting the wall is created by manipulating the x or y cords of our rect or by
                # drawing on the wall.
                visited_cells.append(current_cell)
                pygame.draw.rect(surface=screen,
                                 color=(0, 0, 255),
                                 rect=(maze_block_x_cord, maze_block_y_cord, z, z - line_w)
                                 )

        elif current_cell[0] == maze_width or direction == z:

            if current_cell not in visited_cells:

                if current_cell not in all_cell_into:
                    all_cell_into[current_cell] = "Right"

                visited_cells.append(current_cell)
                pygame.draw.rect(surface=screen,
                                 color=(0, 0, 255),
                                 rect=(maze_block_x_cord - line_w, maze_block_y_cord, z, z - line_w)
                                 )

    elif axis == "y":
        maze_block_y_cord = check_possible_directions_and_go(destination=maze_block_y_cord + direction)
        current_cell = (maze_block_x_cord, maze_block_y_cord)

        if current_cell[1] != maze_height and direction == -z:

            if current_cell not in visited_cells:

                if current_cell not in all_cell_into:
                    all_cell_into[current_cell] = "Up"

                visited_cells.append(current_cell)
                pygame.draw.rect(surface=screen,
                                 color=(0, 0, 255),
                                 rect=(maze_block_x_cord, maze_block_y_cord, z - line_w, z)
                                 )

        elif current_cell[1] == maze_height or direction == z:

            if current_cell not in visited_cells:

                if current_cell not in all_cell_into:
                    all_cell_into[current_cell] = "Down"

                visited_cells.append(current_cell)
                pygame.draw.rect(surface=screen,
                                 color=(0, 0, 255),
                                 rect=(maze_block_x_cord, maze_block_y_cord - line_w, z - line_w, z)
                                 )
    pygame.display.update()


def solve_maze():
    dead_ends = []
    multiple_ways = []
    all_cell_out = {}
    for cell in visited_cells:

        def get_cell_way_into(cell_params):
            try:
                cell_direction_into = all_cell_into[cell_params]
            except KeyError:
                return None

            return cell_direction_into

        # Current cell.
        current = get_cell_way_into(cell_params=cell)

        if current == "Left":
            current = "Right"
        elif current == "Right":
            current = "Left"
        elif current == "Up":
            current = "Down"
        elif current == "Down":
            current = "Up"
        # Cell above.
        above = get_cell_way_into(cell_params=(cell[0], cell[1] - z))
        # Cell on right.
        right = get_cell_way_into(cell_params=(cell[0] + z, cell[1]))
        # Cell below.
        below = get_cell_way_into(cell_params=(cell[0], cell[1] + z))
        # Cell on left.
        left = get_cell_way_into(cell_params=(cell[0] - z, cell[1]))

        all_cell_out[cell] = [current, above, right, below, left]

        if above != "Up":
            all_cell_out[cell].remove(above)
        if right != "Right":
            all_cell_out[cell].remove(right)
        if below != "Down":
            all_cell_out[cell].remove(below)
        if left != "Left":
            all_cell_out[cell].remove(left)

    # Eliminate dead ends
    for cell_dirs in all_cell_out.items():
        if len(cell_dirs[1]) == 1:
            pygame.draw.rect(surface=screen,
                             color=(255, 0, 0),
                             rect=(cell_dirs[0][0], cell_dirs[0][1], z - line_w, z - line_w)
                             )
            dead_ends.append(cell_dirs[0])

    # Find cells with 3 or more ways out.
    for cell_dirs in all_cell_out.items():
        if len(set(cell_dirs[1])) >= 3:
            if (cell_dirs[0][0], cell_dirs[0][1] - z) in dead_ends \
                    or (cell_dirs[0][0], cell_dirs[0][1] + z) in dead_ends \
                    or (cell_dirs[0][0] - z, cell_dirs[0][1]) in dead_ends \
                    or (cell_dirs[0][0] + z, cell_dirs[0][1]) in dead_ends:
                continue
            else:
                pygame.draw.rect(surface=screen,
                                 color=(0, 255, 0),
                                 rect=(cell_dirs[0][0], cell_dirs[0][1], z - line_w, z - line_w)
                                 )
                multiple_ways.append(cell_dirs[0])
    pygame.display.update()


# Game
create_grid()

points = create_points()
start = points[0]
end = points[1]

# If starting point on y axis.
if start[0] == 2:
    down = 0
    sideways = z
# If starting point on x axis.
else:
    down = z
    sideways = 0

# Starting block coordinates.
maze_block_x_cord = start[0] + sideways
maze_block_y_cord = start[1] + down

# Solving block coordinates
solve_block_x_cord = start[0] + sideways
solve_block_y_cord = start[1] + down

# Create starting block.
pygame.draw.rect(surface=screen,
                 color=(0, 0, 255),
                 rect=(maze_block_x_cord, maze_block_y_cord, z - line_w, z - line_w)
                 )

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    while len(visited_cells) != all_cells_n:
        create_maze()
    solve_maze()
    pygame.display.update()
