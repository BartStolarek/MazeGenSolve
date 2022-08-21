from COSC350a2.src.bstolare.agent import Agent


def get_unicode_symbol(unicode):
    unicode_symbols = {'nesw': '┼',
                       'nes-': '├',
                       'ne-w': '┴',
                       '-esw': '┬',
                       '-es-': '┌',
                       'ne--': '└',
                       '-e-w': '─',
                       '-e--': '╶',
                       'n-sw': '┤',
                       'n-s-': '│',
                       'n--w': '┘',
                       '--sw': '┐',
                       '--s-': '╷',
                       'n---': '╵',
                       '---w': '╴'}

    return unicode_symbols[unicode]


class Cell:
    def __init__(self, x, y):
        self.type = "C"
        self.walls = {"north": True, "east": True, "south": True, "west": True}
        self.x = x
        self.y = y

    def get_cell_x_y_as_string(self):
        return "["+str(self.x)+", "+str(self.y)+"]"

    def get_coordinates(self):
        return [self.x, self.y]

    def get_walls(self):
        return self.walls

    def get_code(self):
        code = ""
        if self.walls["north"]:
            code += "n"
        else:
            code += "-"
        if self.walls["east"]:
            code += "e"
        else:
            code += "-"
        if self.walls["south"]:
            code += "s"
        else:
            code += "-"
        if self.walls["west"]:
            code += "w"
        else:
            code += "-"

        return code


    def set_walls(self, code):

        if code[0] == "n":
            self.walls["north"] = True
        elif code[0] == "-":
            self.walls["north"] = False
        else:
            raise ValueError("Cell " + str(self.x) + ", " + str(self.y) + " north part of code is incorrect")

        if code[1] == "e":
            self.walls["east"] = True
        elif code[1] == "-":
            self.walls["east"] = False
        else:
            raise ValueError("Cell " + str(self.x) + ", " + str(self.y) + " east part of code is incorrect")

        if code[2] == "s":
            self.walls["south"] = True
        elif code[2] == "-":
            self.walls["south"] = False
        else:
            raise ValueError("Cell " + str(self.x) + ", " + str(self.y) + " south part of code is incorrect")

        if code[3] == "w":
            self.walls["west"] = True
        elif code[3] == "-":
            self.walls["west"] = False
        else:
            raise ValueError("Cell " + str(self.x) + ", " + str(self.y) + " west part of code is incorrect")


class Vertice:

    def __init__(self, x, y):
        self.type = "V"
        self.symbol = ""
        self.x = x
        self.y = y
        self.walls = {
            "north": True,
            "west": True,
            "south": True,
            "east": True
        }

    def get_code(self):
        code = ""
        if self.walls["north"]:
            code += "n"
        else:
            code += "-"
        if self.walls["east"]:
            code += "e"
        else:
            code += "-"
        if self.walls["south"]:
            code += "s"
        else:
            code += "-"
        if self.walls["west"]:
            code += "w"
        else:
            code += "-"
        return code

    def set_walls(self, code):
        if code[0] == "n":
            self.walls["north"] = True
        elif code[0] == "-":
            self.walls["north"] = False
        else:
            raise ValueError("Vertice " + str(self.x) + ", " + str(self.y) + " north part of code is incorrect")

        if code[1] == "e":
            self.walls["east"] = True
        elif code[1] == "-":
            self.walls["east"] = False
        else:
            raise ValueError("Vertice " + str(self.x) + ", " + str(self.y) + " east part of code is incorrect")

        if code[2] == "s":
            self.walls["south"] = True
        elif code[2] == "-":
            self.walls["south"] = False
        else:
            raise ValueError("Vertice " + str(self.x) + ", " + str(self.y) + " south part of code is incorrect")

        if code[3] == "w":
            self.walls["west"] = True
        elif code[3] == "-":
            self.walls["west"] = False
        else:
            raise ValueError("Vertice " + str(self.x) + ", " + str(self.y) + " west part of code is incorrect")

    def get_symbol(self):
        vertice_code = ""

        if self.walls["north"]:
            vertice_code += "n"
        else:
            vertice_code += "-"
        if self.walls["east"]:
            vertice_code += "e"
        else:
            vertice_code += "-"
        if self.walls["south"]:
            vertice_code += "s"
        else:
            vertice_code += "-"
        if self.walls["west"]:
            vertice_code += "w"
        else:
            vertice_code += "-"
        self.symbol = get_unicode_symbol(vertice_code)
        return self.symbol

    def get_walls(self):
        return self.walls


class Spacer:
    def __init__(self, direction, active: bool, x, y):
        self.type = "S"
        self.direction = direction
        self.walls = {
            "north": True,
            "west": True,
            "south": True,
            "east": True
        }
        self.active = active
        self.x = x
        self.y = y
        if direction == "ns":
            self.symbol = '│'
        else:
            self.symbol = '─'
        if active == False:
            self.symbol = " "

    def get_symbol(self):
        return self.symbol


class Inverse_Maze:
    def __init__(self, maze, spacer):
        print("Initialising inverse maze")
        self.maze = maze
        self.columns = maze.get_x() + 2
        self.rows = maze.get_y() + 2
        self.vertices = []
        self.y_spacer = spacer
        self.x_spacer = spacer * 4
        self.grid = []
        for x in range(0, self.rows):
            row = []
            for y in range(0, self.columns):
                row.append(Vertice(x, y))
            self.vertices.append(row)



    def create_grid(self):

        # For every inverse row except the last
        for x in range(0, self.rows - 1):
            # Add additional spacer rows for each row
            for j in range(0, self.y_spacer):

                # Start with empty string
                y_spacer = []

                # Make the two spacer rows above each row, column by column
                for y in range(0, self.columns - 1):
                    # add cells two spacers first
                    for i in range(0, self.x_spacer):
                        spacer_active = self.vertices[x][y].get_walls()["north"]
                        y_spacer.append(Spacer("ns", False, x, y))
                    if x == 0:
                        y_spacer.append(Spacer("ns", False, x, y))
                    else:

                        y_spacer.append(Spacer("ns", spacer_active, x, y))

                # Print spacers
                self.grid.append(y_spacer)
            row = []

            # Make rows WE walls
            for y in range(0, self.columns - 1):
                # Add cell's two spacers first
                for i in range(0, self.x_spacer):

                    if y == 0:
                        spacer = Spacer("we", False, x, y)
                        row.append(spacer)

                    else:
                        spacer_active= self.vertices[x][y].get_walls()["west"]
                        spacer = Spacer("we", spacer_active, x, y)
                        row.append(spacer)

                row.append(self.vertices[x][y])

            self.grid.append(row)


    def print_grid(self):

        rows = len(self.grid)
        columns = len(self.grid[0])

        for x in range(0, rows):
            row = ""
            for y in range(0, columns):
                row += self.grid[x][y].get_symbol()
            print(row)



    def map_cells_to_vertices(self):
        x_length = len(self.vertices) - 1
        y_length = len(self.vertices[0]) - 1
        # Set inner vertices
        for x in range(1, x_length - 1):
            for y in range(1, y_length - 1):
                top_left_cell_walls = self.maze.get_cell(x - 1, y - 1).get_walls()
                bottom_right_cell_walls = self.maze.get_cell(x, y).get_walls()

                if top_left_cell_walls["south"]:
                    w = "w"
                else:
                    w = '-'
                if top_left_cell_walls["east"]:
                    n = "n"
                else:
                    n = '-'
                if bottom_right_cell_walls["north"]:
                    e = "e"
                else:
                    e = '-'
                if bottom_right_cell_walls["west"]:
                    s = "s"
                else:
                    s = '-'

                code = n + e + s + w

                self.vertices[x][y].set_walls(code)
        x = 0
        y = 0
        # Set top rows inner vertices
        for y in range(1,y_length-1):
            bottom_left_cell_walls = self.maze.get_cell(0, y-1).get_walls()
            bottom_right_cell_walls = self.maze.get_cell(0, y).get_walls()
            code = "-"
            if bottom_right_cell_walls["north"]:
                code += "e"
            else:
                code += "-"
            if bottom_right_cell_walls["west"]:
                code += "s"
            else:
                code += "-"
            if bottom_left_cell_walls["north"]:
                code += "w"
            else:
                code += "-"

            self.vertices[x][y].set_walls(code)
        x = 0
        y = 0
        for x in range(1,x_length-1):
            top_right_cell_walls = self.maze.get_cell(x-1, 0).get_walls()
            bottom_right_cell_walls = self.maze.get_cell(x, 0).get_walls()
            code = ""
            if top_right_cell_walls["west"]:
                code += "n"
            else:
                code += "-"
            if top_right_cell_walls["south"]:
                code += "e"
            else:
                code += "-"
            if bottom_right_cell_walls["west"]:
                code += "s"
            else:
                code += "-"

            code += "-"

            self.vertices[x][y].set_walls(code)
        x = 0
        y = 0

        # Remove outward facings wicks from outer boundary

        for x in range(0, x_length):
            self.vertices[x][0].walls["west"] = False
            self.vertices[x][y_length - 1].walls["east"] = False
        x = 0
        y = 0
        for y in range(0, y_length):
            self.vertices[0][y].walls["north"] = False
            self.vertices[x_length - 1][y].walls["south"] = False
        x = 0
        y = 0
        # Top boundary vertices update
        for y in range(0, y_length - 1):
            self.vertices[0][y].walls["east"] = self.maze.get_cell(0, y).get_walls()["north"]
            self.vertices[0][y].walls["south"] = self.maze.get_cell(0, y).get_walls()["west"]
            vertice_check = self.vertices[0][y].walls


        x = 0
        y = 0
        # Right boundary vertices update
        for x in range(0, x_length - 1):
            self.vertices[x][y_length - 1].walls["west"] = self.maze.get_cell(x, y_length - 2).get_walls()["north"]
            self.vertices[x][y_length - 1].walls["south"] = self.maze.get_cell(x, y_length - 2).get_walls()["east"]
        x = 0
        y = 0
        # Bottom boundary vertices update
        for y in range(y_length - 1, 0, -1):
            self.vertices[x_length - 1][y].walls["north"] = self.maze.get_cell(x_length - 2, y - 1).get_walls()["east"]
            self.vertices[x_length - 1][y].walls["west"] = self.maze.get_cell(x_length - 2, y - 1).get_walls()["south"]
        x = 0
        y = 0
        # Left boundary vertices update
        for x in range(x_length - 1, 0, -1):
            self.vertices[x][0].walls["north"] = self.maze.get_cell(x - 1, 0).get_walls()["west"]
            self.vertices[x][0].walls["east"] = self.maze.get_cell(x - 1, 0).get_walls()["south"]

    def print_vertice_x_y(self):
        for x in range(0, len(self.vertices)):
            row = []
            for y in range(0, len(self.vertices[0])):
                row.append(self.vertices[x][y].type + "(" + str(self.vertices[x][y].x) + ", " + str(
                    self.vertices[x][y].y) + "/" + self.vertices[x][y].get_code() + ")")
            print(row)

    def print_grid_x_y(self):
        for x in range(0, len(self.grid)):
            row = []
            for y in range(0, len(self.grid[0])):
                if self.grid[x][y].type == "S":
                    if self.grid[x][y].active:
                        code = self.grid[x][y].direction
                    else:
                        code = "--"
                else:
                    code = self.grid[x][y].get_code()
                row.append(self.grid[x][y].type + "(" + str(self.grid[x][y].x) + ", " + str(self.grid[x][y].y) +"/" + code+ ")")
            print(row)



class Maze:
    def __init__(self, rows, columns):
        print("Initialising maze")
        self.rows = rows
        self.columns = columns
        self.cells = []



    def get_cell(self, x, y):
        return self.cells[x][y]

    def get_x(self):
        return self.columns

    def get_y(self):
        return self.rows

    def make_maze(self, maze):
        print("Making the maze")
        self.cells = []
        for x in range(0, self.rows):
            column = []
            for y in range(0, self.columns):
                cell = Cell(x, y)
                cell.set_walls(maze[x][y])

                column.append(cell)
            self.cells.append(column)

    def print_cell_maze(self):

        for x in range(0, self.rows):
            row = ""
            for y in range(0, self.columns):
                row += "C("+str(x)+", "+str(y)+"/"+str(self.cells[x][y].get_code())+"), "
            print(row)



def main():
    row0 = ["n--w", "n-s-", "ne--", "n--w", "n-s-", "ne--", "n--w", "n-s-", "n-s-", "ne--"]
    row1 = ["-e-w", "n-sw", "-es-", "--sw", "ne--", "--sw", "-e--", "ne-w", "n--w", "-es-"]
    row2 = ["--sw", "ne--", "n--w", "nes-", "---w", "ne--", "--sw", "-es-", "-e-w", "ne-w"]
    row3 = ["n--w", "--s-", "-es-", "n--w", "-e--", "--sw", "nes-", "n--w", "--s-", "-es-"]
    row4 = ["--sw", "n-s-", "n-s-", "-es-", "--sw", "nes-", "n-sw", "--s-", "n-s-", "nes-"]

    size = [5,10]

    start = [0, 0]
    end = [size[0]-1, size[1]-1]

    # Hyper parameters
    episodes = 500
    gamma = 0.5 # interest in neighbours (discount value)
    alpha = 0.5 # rate of learning


    custom_maze = [row0, row1, row2, row3, row4]
    maze = Maze(size[0], size[1])
    maze.make_maze(custom_maze)



    inverse_maze = Inverse_Maze(maze, 1)




    inverse_maze.map_cells_to_vertices()


    inverse_maze.create_grid()


    print("CELL MAZE")
    inverse_maze.maze.print_cell_maze()
    print("VERTICE MAZE")
    inverse_maze.print_vertice_x_y()
    print("LAYOUT")
    inverse_maze.print_grid_x_y()
    print("END MAZE")
    inverse_maze.print_grid()

    agent = Agent(maze,start, end, episodes, gamma, alpha )

    agent.print_rewards_map()
    agent.tdl()
    agent.print_values_map()



if __name__ == '__main__':
    main()
