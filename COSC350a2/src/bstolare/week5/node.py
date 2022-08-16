# Node in Bayes Network
class Node:
    def __init__(self,variable):
        #cpt is a dictionary of truth table values e.g. cpt["tt"] = 0.1
        self.variable = variable
        self.children = []
        self.cpt = {}
        
    def add_cpt(self,expression,value): 
        # adds key expression with value to dictionary.
        self.cpt[expression] = value
        
    def get_cpt(self):
        return dict(self.cpt)
    
    def get_name(self):
        return self.variable
    
    def add_child(self,child):
        self.children.append(child)
        
    def get_children(self):
        return list(self.children)
    
    def __str__(self):
        return self.variable + ": " + str(self.cpt)
