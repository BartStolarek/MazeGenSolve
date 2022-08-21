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
            return "up"
        elif i == 1:
            return "down"
        elif i == 2:
            return "left"
        elif i == 3:
            return "right"

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
            print("episode: " + str(i))
            cell = self.start
            while True:
                print("state: " + str(cell.x) + ", " + str(cell.y))
                action = self.get_action(cell)
                print("got action: " + action)
                reward, next_cell = self.take_action(cell, action)
                print("got reward: " + str(reward) + " next cell: [" + str(next_cell.x) + ", " + str(next_cell.y)+"]")



                if next_cell.get_coordinates() == self.end:
                    break

                # V(S) = V(S) + alpha * (reward_of_new_state + gamma * V(new_state) - V(current_state))
                current_value = self.values[cell.x][cell.y]
                after = self.values[cell.x][cell.y]


                self.values[cell.x][cell.y] = self.values[cell.x][cell.y] + self.alpha * (reward + self.gamma * after - current_value)

                cell = next_cell






