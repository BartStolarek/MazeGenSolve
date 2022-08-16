""" 
    Graph: animated graph with Tkinter.
    COSC350/550 Workshop 3
"""

import time
from tkinter import *
from PIL import ImageTk, Image
from random import randint
import sys

# Start global variables #
quit = False
width = 500
height = 500
node_size = 10
delay = 0.05
inter = 0
"""
0 Armidale 330,50
1 Tarmworth 250,125
2 Dubbo 10,270
3 Bathurst 115,415
4 Sydney 280,475
5 Newcastle 334,334

"""
# node - adjacency list with distances (all potentially connected)
node_graph = {0: [0,95,348,378,375,268],
              1: [95,0,254,288,309,219],
              2: [348,254,0,158,301,306],
              3: [378,288,158,0,159,212],
              4: [375,309,301,159,0,117],
              5: [268,219,306,212,117,0]}

# node locations:
node_locs = [[330,50],[250,125],[10,270],[115,415],[280,475],[334,334]]


visited = []
explored = []
node_items = []
# End global variables #

def create_node(x, y, r, canvasName,colour,obj_tag): 
    "Create circle with fill colour: (x,y): center coordinates, r: radius "
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill=colour,tag=obj_tag)

def create_branch(x0, y0, x1, y1, canvasName,colour,obj_tag): 
    "Create line with fill colour: (x0,y0 to x1,y1): "
    return canvasName.create_line(x0, y0, x1, y1,fill=colour,width=3,tag=obj_tag)

def create_plot(myCanvas):
    " Create initial plot with graph nodes  "
    global node_size
    global node_locs
    global visited
    global node_items
    
    #delete before redraw                              
    for item in node_items:                             
       myCanvas.delete(item)   
       
    node_label = 1
    #draw/redraw nodes
    for x,y in node_locs:
        node_name = "n"+str(x)+str(y)
        if node_name in visited:
            create_node(x,y,node_size,myCanvas,"darkred",node_name)
        else:
            create_node(x,y,node_size,myCanvas,"red",node_name)
        text_name = "t"+str(node_label)
        myCanvas.create_text(x, y, text=str(node_label),tag=text_name, font=(20) )
        node_label = node_label + 1
        if node_name not in node_items:
            node_items.append(node_name)
            node_items.append(node_label)

def init_cities(start,moves):
    "Generates initial random path for TSP"
    visited.append(start)
    while len(visited) <= moves:
        ran_move = randint(0,moves)
        if ran_move not in visited:
            visited.append(ran_move)
    visited.append(start)        
    return visited        

def calc_distance(graph,visited):
    #calculates distance between all cities in path.
    distance = 0
    for i in range(len(visited)-1):
        distance = distance + graph[visited[i]][visited[i+1]]

    return distance

def swap_cities(visited):
    " Swaps two cities in the visited list - avoid start and stop (armidale) "
    visited = list(visited)
    pair = [] 
    while len(pair) < 2:
        ran_move = randint(1,5)
        if ran_move not in pair:
            pair.append(ran_move)
    
    visited[pair[0]], visited[pair[1]] = visited[pair[1]], visited[pair[0]]
    
    return visited
    
def shc(graph,iterations,visited):
    # Stochastic hill climb search
    min_dist = calc_distance(graph,visited)
    for i in range(iterations):
       city_swap = swap_cities((visited))
       new_dist = calc_distance(graph,city_swap)
       if new_dist < min_dist:
           visited = (city_swap)
           min_dist = new_dist
    
    return visited
        
def run_plot():
    " Main feed-back loop : animates tree-graph "
    global quit
    global node_locs
    global inter
    global visited
    #stack = queue()
    if quit or inter == 6:
        quit = True
        return 
    create_branch(node_locs[visited[inter]][0],node_locs[visited[inter]][1],
                              node_locs[visited[inter+1]][0],node_locs[visited[inter+1]][1],myCanvas,"black","C"+str(inter))
    create_plot(myCanvas) 
    if not quit:
        inter = inter + 1
        myCanvas.after(500, run_plot)

def close_properly(root):
    global quit
    if quit==False:
        quit = True
    else:
        root.destroy()
    
def on_closing():
    global quit
    if quit==False:
        quit = True
    else:
        root.destroy()
 
root = Tk()
root.title("Travelling Salesperson") 
map = ImageTk.PhotoImage(Image.open("map.png"))
myCanvas = Canvas(root, width=width, heigh=height, borderwidth=0, highlightthickness=0, bg="white")
myCanvas.pack()
Canvas_Image = myCanvas.create_image(0,0, image=map, anchor="nw")

def main():
    " Main function: call and report... "
    global node_grah
    global visited
    create_plot(myCanvas)
    
    Button(root, text="Quit", command = lambda: close_properly(root)).pack()
    
    
    visited = init_cities(0,5)
    #visited = [0, 1, 2, 3, 4, 5, 0]
    print("Start order:",visited,"distance:",calc_distance(node_graph,visited))
    visited = shc(node_graph,1000,visited)
    print("End order:",visited,"distance:",calc_distance(node_graph,visited))
    
    run_plot()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
    
if __name__ == "__main__":
    main()
