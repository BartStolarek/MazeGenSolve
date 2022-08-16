class Cell:

    def __init__(self, x, y):

        self.walls = {"north": True, "east": True,"south": True, "west": True}
        self.x = x
        self.y = y

    def get_walls(self):
        return self.walls


class Vertice:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.walls = {
            "north": True,
            "west": True,
            "south": True,
            "east": True
        }

    def get_walls(self):

        return self.walls



class Inverse_Maze:


    def __init__(self, maze,spacer):
        print("Initialising inverse maze")
        self.maze = maze
        self.columns = maze.get_x()+2
        self.rows = maze.get_y()+2
        self.vertices = []
        self.y_spacer = spacer
        self.x_spacer = spacer * 4
        for x in range(0, self.rows):
            row = []
            for y in range(0, self.columns):

                row.append(Vertice(x, y))
            self.vertices.append(row)

    def get_spacer(self,direction):
        if direction == "ns":
            return '│'
        else:
            return '─'

    def get_vertices(self):
        print("Getting inverse maze vertices")
        return self.vertices

    def print_grid(self):
        print("Printing Inverse Maze")
        print(self.get_vertice(0,0))

        # For every inverse row except the last
        for x in range(0, self.rows-1):

            # Add additional spacer rows for each row
            for j in range(0, self.y_spacer):

                # Start with empty string
                y_spacer = str(x)+""

                # Make the two spacer rows above each row, column by column
                for y in range(0, self.columns-1):
                    # add cells two spacers first
                    for i in range(0, self.x_spacer):
                        y_spacer += " "
                    if x == 0:
                        y_spacer += " "
                    else:
                        y_spacer += self.get_spacer("ns")

                # Print spacers
                print(y_spacer)
                row = str(x)+""

            # Make rows WE walls
            for y in range(0, self.columns-1):
                # Add cell's two spacers first
                for i in range(0, self.x_spacer):
                    if y == 0:
                        row += " "
                    else:
                        row += self.get_spacer("we")
                row += self.get_vertice(x, y)
            print(row)

    def get_unicode_symbol(self,unicode):
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

    def get_vertice(self, x, y):

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

        return self.get_unicode_symbol(vertice_code)




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
    inverse_maze.print_grid()



if __name__ == '__main__':
    main()
