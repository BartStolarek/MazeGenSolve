import random

class Agent:
    def __init__(self, maze, start, end, episodes, gamma, alpha):
        # Hyper parameters
        self.episodes = episodes
        self.gamma = gamma # interest in neighbours (discount value)
        self.alpha = alpha # rate of learning
        self.maze = maze
        self.start = self.maze.cells[start[0]][start[1]]
        self.end = end
        self.path = []
        self.rewards_map = []
        for x in range(0, self.maze.rows):
            row = []
            for y in range(0, self.maze.columns):
                reward = ((x - end[0]) + (y - end[1]))/2
                if reward > 0 :
                    reward = reward * -1
                row.append(reward)
            self.rewards_map.append(row)


        self.values = []
        for x in range(0, maze.rows):
            row = []
            for y in range(0, maze.columns):
                value = 0
                row.append(value)
            self.values.append(row)


    def print_rewards_map(self):
        for x in range(len(self.rewards_map)):
            print(str(self.rewards_map[x]))


    def print_values_map(self):
        for x in range(len(self.values)):
            print(str(self.values[x]))

    def get_move_text(self, i):
        if i == 0:
            return "north"
        elif i == 1:
            return "east"
        elif i == 2:
            return "south"
        elif i == 3:
            return "west"

    def check_if_valid_move(self, cell, direction):
        return not cell.walls[direction]

    def get_action(self, cell):
        move = ""
        while True:
            i = random.randint(0, 3)
            if i == 0:
                move = "north"
                if self.check_if_valid_move(cell, move):
                    break
            elif i == 1:
                move = "east"
                if self.check_if_valid_move(cell, move):
                    break
            elif i == 2:
                move = "south"
                if self.check_if_valid_move(cell, move):
                    break
            elif i == 3:
                move = "west"
                if self.check_if_valid_move(cell, move):
                    break
        return move

    def take_action(self, cell, action):
        x = cell.x
        y = cell.y
        if action == "north":
            x = x - 1
        elif action == "east":
            y = y + 1
        elif action == "south":
            x = x + 1
        elif action == "west":
            y = y - 1

        return self.rewards_map[x][y], self.maze.cells[x][y]

    def get_random_state(self):
        x = random.randint(0, self.maze.rows-1)
        y = random.randint(0, self.maze.columns-1)

        return [x, y]

    def tdl(self):

        for i in range(0, self.episodes):
            cell = self.start
            while True:
                action = self.get_action(cell)
                reward, next_cell = self.take_action(cell, action)

                if next_cell.get_coordinates() == self.end:
                    break

                # V(S) = V(S) + alpha * (reward_of_new_state + gamma * V(new_state) - V(current_state))
                current_value = self.values[cell.x][cell.y]
                after = self.values[cell.x][cell.y]

                self.values[cell.x][cell.y] = round(self.values[cell.x][cell.y] + self.alpha * (reward + self.gamma * after - current_value),3)

                cell = next_cell


    def get_path(self,backtracking=True, max_attempts=0):
        travelled = []
        travelled.append(self.start)
        cell = self.start
        if backtracking:

            ignore = ""
            back_tracks = 0
            for cells in range(0, len(self.maze.cells)*len(self.maze.cells[0])):

                best_value = -1000000
                best_cell = ""
                best_direction = ""
                valid_moves = 0
                next_cell = cell

                # For current cell, check all four moves
                for i in range(0,4):

                    # Get the direction
                    direction = self.get_move_text(i)

                    # If valid move then get next cell
                    if self.check_if_valid_move(cell, direction) and direction != ignore:

                        rewards, next_cell = self.take_action(cell, direction)
                        # If the next cells value is greater than the current best, and next cell has not been travelled
                        # create new best values
                        if self.values[next_cell.x][next_cell.y] > best_value and next_cell not in travelled:

                            valid_moves = valid_moves + 1
                            best_value = self.values[next_cell.x][next_cell.y]
                            best_cell = next_cell
                            best_direction = direction

                    if next_cell.get_coordinates() == self.end:
                        return back_tracks

                if valid_moves == 0:
                    travelled.pop()
                    ignore = self.path.pop()
                    cell = travelled[-1]
                    back_tracks = back_tracks + 1

                else:
                    self.path.append(best_direction)
                    travelled.append(best_cell)
                    cell = best_cell
                    ignore = ""

        else:
            dead_ends = []
            attempts = 0
            while attempts < max_attempts:

                best_value = -1000000
                best_cell = ""
                best_direction = ""
                valid_moves = 0
                next_cell = cell

                print(str(attempts) + " " + str(self.path))
                # For current cell, check all four moves
                for i in range(0,4):

                    # Get the direction
                    direction = self.get_move_text(i)

                    # If valid move then get next cell
                    if self.check_if_valid_move(cell, direction):

                        rewards, next_cell = self.take_action(cell, direction)
                        # If the next cells value is greater than the current best, and next cell has not been travelled
                        # create new best values
                        if self.values[next_cell.x][next_cell.y] > best_value and next_cell not in travelled and next_cell not in dead_ends:
                            valid_moves = valid_moves + 1
                            best_value = self.values[next_cell.x][next_cell.y]
                            best_cell = next_cell
                            best_direction = direction

                    if next_cell.get_coordinates() == self.end:
                        return attempts

                if valid_moves == 0:
                    self.path = []
                    travelled = []
                    dead_ends.append(cell)
                    cell = self.start
                    attempts = attempts + 1
                else:
                    self.path.append(best_direction)
                    travelled.append(best_cell)
                    cell = best_cell

















