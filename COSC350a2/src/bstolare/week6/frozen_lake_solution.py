import random
from tkinter import *
from PIL import ImageTk, Image
import time

# Initialise Globals:
grid_w = 8
grid_h = 8
root = Tk()
imgs = [0 for i in range(4)]
labels  = []
quit = False
inter = 0
iterations = 0
start = [0,0]
goal = [7,7]
path = []

up = [-1,0]
down = [1,0]
left = [0,-1]
right = [0,1]
directions = [up,down,left,right]
rewards_map = [[-0.5,-0.01,-0.01,-0.01,-0.01,-0.01,-0.01,-0.01],
               [-0.01,-0.01,-0.01,-0.01,-0.01,-0.01,-0.01,-0.01],
               [-0.01,-0.01,-0.9,-0.9,-0.01,-0.01,-0.9,-0.9],
               [-0.01,-0.01,-0.9,-0.9,-0.01,-0.01,-0.9,-0.9],
               [-0.01,-0.01,-0.01,-0.01,-0.01,-0.01,-0.9,-0.9],
               [-0.01,-0.01,-0.01,-0.01,-0.01,-0.01,-0.9,-0.9],
               [-0.9,-0.9,-0.01,-0.01,-0.01,-0.01,-0.01,-0.01],
               [-0.9,-0.9,-0.01,-0.01,-0.01,-0.01,-0.01,0.1]]

lake_map = [['s','f','f','f','f','f','f','f'],
            ['f','f','f','f','f','f','f','f'],
            ['f','f','h','h','f','f','h','h'],
            ['f','f','h','h','f','f','h','h'],
            ['f','f','f','f','f','f','h','h'],
            ['f','f','f','f','f','f','h','h'],
            ['h','h','f','f','f','f','f','f'],
            ['h','h','f','f','f','f','f','g']]


# End Globals

def this_move(i):
    if i == 0:
        return "up"
    elif i == 1:
        return "down"
    elif i == 2:
        return "left"
    elif i == 3:
        return "right"

def valid_move(state,i):
    global directions
    # 3 is the dimensions
    x = state[0] + directions[i][0]
    y =  state[1] + directions[i][1]
    if x < 0 or x > 7 or y < 0 or y > 7:
        return False
    #print("xy",x,y)
    return True

def get_action(state):
    move = -1
    while True:
        move = random.randint(0,3)
        if valid_move(state,move):
            break
    return move

def take_action(state,action):
    global rewards_map
    #print(">",state,action)
    x = state[0] + directions[action][0]
    y =  state[1] + directions[action][1]
   # print("xy",x,y)
    return rewards_map[x][y],[x,y]

def get_random_state():
    global grid_w
    global grid_h
    x = random.randint(0,grid_w-1)
    y = random.randint(0,grid_h-1)
    
    return [x,y]

def mcs(goal):
    episodes =500
    gamma =0.25
    #initialise model S_t
    values = [ [0] * grid_w for _ in range(grid_h)]

    for i in range(episodes):
        G = 0.0
        start = get_random_state()
        state = list(start)
        visited_states = []
        while True:
            action = get_action(state)
            reward, new_state = take_action(state,action)
            
            if new_state not in visited_states:
                # G <- yG + R_t+1
                G += gamma * G + reward
                visited_states.append(new_state)
            state = list(new_state)
            if new_state == goal:
                break
                
        if visited_states:
            ave = G / len(visited_states)
            if ave > values[start[0]][start[1]] or values[start[0]][start[1]] == 0:
                values[start[0]][start[1]] = ave
            
                
    return values





def tdl(state,goal):
    # note: adjusting gamma causes infinite loop.
    
    episodes = 500
    gamma = 0.1
    alpha = 0.5

    values = [ [0] * grid_w for _ in range(grid_h)]
    
    for i in range(episodes):
        start = list(state)
        while True: 
            action = get_action(state)
            reward, new_state = take_action(state,action)
            
            if new_state == goal:
                break

            # V(S) = V(S) + aplha * (reward' + gamma * V(S') - V(S))
            current = values[state[0]][state[1]]
            after = values[new_state[0]][new_state[1]]
            values[state[0]][state[1]] += alpha * (reward + gamma * after - current)
            
            state = list(new_state)
                
    
    return values

def get_path(state,goal,values):
    path = []
    travelled = []
    travelled.append(state)
    max_attempts = 100
    for j in range(max_attempts):
        max_val = -10.0
        max_state = [0,0]
        max_move = 0
        for i in range(4):
            if valid_move(state,i):
                rewards,new_state = take_action(state,i)
                #print(new_state)
                if values[new_state[0]][new_state[1]] > max_val and new_state not in travelled:
                    max_val = values[new_state[0]][new_state[1]]
                    max_state = list(new_state)
                    max_move = i
    
        path.append(max_move)
        travelled.append(max_state)
        state = list(max_state)
        #print(state)
        if state == goal:
            return path
    print("Max pathing attempts reach - exiting")
    exit()
    return path

def place_images(lock):
    " Place images in locations - highlight lock"
    global lake_map
    global grid_w
    global grid_h
    global labels
    
    for i in range(grid_w):
        row = []
        for j in range(grid_h):
            if lake_map[i][j] == 's' and lock == [i,j]:
                label_t = Label(root, image = imgs[0], highlightthickness=4, highlightbackground="blue")
                label_t.grid(row=i, column=j)
            elif lake_map[i][j] == 'f' and lock == [i,j]:
                label_t = Label(root, image = imgs[1], highlightthickness=4, highlightbackground="blue")
                label_t.grid(row=i, column=j)
            elif lake_map[i][j] == 'h' and lock == [i,j]:
                label_t = Label(root, image = imgs[2], highlightthickness=4, highlightbackground="blue")
                label_t.grid(row=i, column=j)
            elif lake_map[i][j] == 'g' and lock == [i,j]:
                label_t = Label(root, image = imgs[3], highlightthickness=4, highlightbackground="blue")
                label_t.grid(row=i, column=j)
            elif lake_map[i][j] == 's':
                label_t = Label(root, image = imgs[0], highlightthickness=4)
                label_t.grid(row=i, column=j)
            elif lake_map[i][j] == 'f':
                label_t = Label(root, image = imgs[1], highlightthickness=4)
                label_t.grid(row=i, column=j)
            elif lake_map[i][j] == 'h':
                label_t = Label(root, image = imgs[2], highlightthickness=4)
                label_t.grid(row=i, column=j)
            elif lake_map[i][j] == 'g':
                label_t = Label(root, image = imgs[3], highlightthickness=4)
                label_t.grid(row=i, column=j)
            row.append(label_t)
        labels.append(row)
    root.update()

lock =[0,0]
def show_path():
    global quit
    global inter
    global iterations
    global path
    global root
    global lock
    global labels
    if quit or inter == iterations:
        quit = True
    labels[lock[0]][lock[1]].config(highlightbackground="grey")
    reward,new_state = take_action(lock,path[inter])
    #print(new_state,path[i])
    lock = list(new_state)
    labels[lock[0]][lock[1]].config(highlightbackground="blue")
    if not quit:
       inter = inter + 1
       root.after(500, show_path)


def on_closing():
    global quit
    if quit==False:
        quit = True
        root.after(50, on_closing)
    else:
        root.destroy()

def main():
    # main function - call and report
    
    global rewards_map
    global iterations
    global path

    root.title("Frozen Lake")
    imgs[0] = ImageTk.PhotoImage(Image.open("images/start.png"))
    imgs[1] = ImageTk.PhotoImage(Image.open("images/frozen.png"))
    imgs[2] = ImageTk.PhotoImage(Image.open("images/melt.png"))
    imgs[3] = ImageTk.PhotoImage(Image.open("images/goal.png"))
    
    
    place_images([0,0])
    

    #Print rewards map:
    print("Rewards Map:")
    for row in rewards_map:
        for cell in row:
            print(str(cell)+" ",end="")
        print()
    
    #values = mcs(goal)
    values = tdl(start,goal)
    print("Optimal values:")
    for row in values:
        for cell in row:
            print(str(round(cell,2))+" ",end="")
        print()
        
    print("Optimal path")
    path = get_path(start,goal,values)
    print(len(path),path)
    iterations = len(path)-1
    show_path()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
    


if __name__ == "__main__":
    main()
