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
        self.walls = {"north": True, "east": True, "south": True, "west": True}
        self.x = x
        self.y = y

    def get_walls(self):
        return self.walls


class Vertice:

    def __init__(self, x, y):
        self.symbol = ""
        self.x = x
        self.y = y
        self.walls = {
            "north": True,
            "west": True,
            "south": True,
            "east": True
        }

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
    def __init__(self, direction, active: bool):
        self.direction = direction
        self.active = active
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

    def get_spacer(self, direction):
        if direction == "ns":
            return '│'
        else:
            return '─'

    def get_vertices(self):
        print("Getting inverse maze vertices")
        return self.vertices

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
                        y_spacer.append(Spacer("ns", False))
                    if x == 0:
                        y_spacer.append(Spacer("ns", False))
                    else:
                        y_spacer.append(Spacer("ns", True))

                # Print spacers
                self.grid.append(y_spacer)
            row = []

            # Make rows WE walls
            for y in range(0, self.columns - 1):
                # Add cell's two spacers first
                for i in range(0, self.x_spacer):
                    if y == 0:
                        row.append(Spacer("we", False))
                    else:
                        row.append(Spacer("we", True))
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

    def dep_print_grid(self):
        print("Printing Inverse Maze")
        print(self.get_vertice_symbol(0, 0))

        # For every inverse row except the last
        for x in range(0, self.rows - 1):
            # Add additional spacer rows for each row
            for j in range(0, self.y_spacer):

                # Start with empty string
                y_spacer = str(x) + ""

                # Make the two spacer rows above each row, column by column
                for y in range(0, self.columns - 1):
                    # add cells two spacers first
                    for i in range(0, self.x_spacer):
                        y_spacer += " "
                    if x == 0:
                        y_spacer += " "
                    else:
                        y_spacer += self.get_spacer("ns")

                # Print spacers
                print(y_spacer)
            row = str(x) + ""

            # Make rows WE walls
            for y in range(0, self.columns - 1):
                # Add cell's two spacers first
                for i in range(0, self.x_spacer):
                    if y == 0:
                        row += " "
                    else:
                        row += self.get_spacer("we")
                row += self.get_vertice_symbol(x, y)
            print(row)

    def get_vertice_symbol(self, x, y):

        vertice_walls = self.vertices[x][y].get_walls()
        vertice_code = ""

        if vertice_walls["north"]:
            vertice_code += "n"
        else:
            vertice_code += "-"
        if vertice_walls["east"]:
            vertice_code += "e"
        else:
            vertice_code += "-"
        if vertice_walls["south"]:
            vertice_code += "s"
        else:
            vertice_code += "-"
        if vertice_walls["west"]:
            vertice_code += "w"
        else:
            vertice_code += "-"

        return get_unicode_symbol(vertice_code)


class Maze:
    def __init__(self, rows, columns):
        print("Initialising maze")
        self.rows = rows
        self.columns = columns
        self.cells = []
        self.vertices = []

    def get_x(self):
        return self.columns

    def get_y(self):
        return self.rows

    def make_maze(self):
        print("Making the maze")
        self.cells = []
        for i in range(0, self.rows):
            column = []
            for j in range(0, self.columns):
                cell = Cell(j, i)
                column.append(cell)
            self.cells.append(column)


def main():
    columns = 10
    rows = 5

    maze = Maze(5, 10)
    maze.make_maze()
    inverse_maze = Inverse_Maze(maze, 2)
    inverse_maze.create_grid()
    inverse_maze.print_grid2()


if __name__ == '__main__':
    main()
