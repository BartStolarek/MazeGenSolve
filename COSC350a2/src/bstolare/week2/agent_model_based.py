""" 
    Agent Class: simple agent demonstration.
    COSC350/550 Workshop 2
"""

class Agent:
    def __init__(self,tag,colour,speed,x,y,width,height,radius):
        self.tag = tag
        self.colour = colour
        self.speed = speed
        self.x = x
        self.y = y
        self.p_moves = 0 # p = peripheral
        # create internal model (tracks movements)
        # creates a reduced grid of environment
        self.model_w = round(width/radius)
        self.model_h = round(height/radius)
        self.model = [[0 for i in range(self.model_w)] for i in range(self.model_h)]
        self.size=radius
        #print(self.model)

    def print_details(self):
        print("Tag: ", self.tag)
        print("Colour: ", self.colour)
        print("Speed: ", self.speed)
        print("location: ("+str(self.x)+","+str(self.x)+")")
    
    def get_colour(self):
        return self.colour
    
    def get_speed(self):
        return self.speed
    
    def get_tag(self):
        return self.tag
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
        
    def set_x(self,new_x):
        self.x = new_x
    
    def set_y(self,new_y):
        self.y = new_y

    def check_model(self):
        "Checks if all locations in model searched"
        for i in range(self.model_w):
            for j in range(self.model_h):
                if self.model[i][j] == 0:
                     return False
        return True
    
    				 
        
    def program(self,status,location):
        "Black box"
	# Keep track of locations searched
        model_x = round(location[0]/self.size)
        model_y = round(location[1]/self.size)
        
        if self.check_model():
            return "stop"
        elif status == "odd":
            self.model[model_x][model_y] = 1
            return "eat"
        elif status == 'even':
            self.model[model_x][model_y] = 1
            return "interact"
        else: 
            return "move"

