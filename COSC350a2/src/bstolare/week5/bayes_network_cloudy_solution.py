# Discrete Bayesian Network - Algorithm - P 514 on prescribed text
from node import Node

def make_model():
    # Remember that the models do not include false values, you will need to calculate these.
    model = []
    c = Node("Cloudy")
    c.add_cpt("T",0.5)
    c.add_cpt("F",0.5)
    
    model.append(c)
    
    s = Node("Sprinkler")
    s.add_cpt("TT",0.1)
    s.add_cpt("TF",0.9)
    s.add_cpt("FT",0.5)
    s.add_cpt("FF",0.5)
    
    model.append(s)
    c.add_child(s)
    
    r = Node("Rain")
    r.add_cpt("TT",0.8)
    r.add_cpt("TF",0.2)
    r.add_cpt("FT",0.2)
    r.add_cpt("FF",0.8)
    
    model.append(r)
    c.add_child(r)
    
    g = Node("Wet Grass")
    g.add_cpt("TTT",0.99)
    g.add_cpt("TTF",0.01)
    g.add_cpt("TFT",0.9)
    g.add_cpt("TFF",0.1)
    g.add_cpt("FTT",0.9)
    g.add_cpt("FTF",0.1)
    g.add_cpt("FFT",0.0)
    g.add_cpt("FFF",1.0)
    
    model.append(g)
    s.add_child(g)
    r.add_child(g)
    
    
    return model

def classify_casual(model,infer):
    prob = 1.0
    queue = []
    p_count = 0
    
    # append all parent nodes until child node found
    while model[p_count] not in model[0].get_children():
        queue.append(model[p_count])
        p_count += 1
    
    # we can use a queue to read the successive child of each parent
    while queue:
        parent = queue.pop(0)
        cpt = parent.get_cpt()
        if parent.get_name() in infer:
            expression = infer[parent.get_name()]
            prob *= cpt[ expression ]
        for child in parent.get_children():
            if child not in queue:
                queue.append(child)
        
        
    return prob

def main():
    # main function - call and report
    
    model = make_model()
    """
    for node in model:
        print(str(node))
    """
    infer = {"Cloudy":"T","Sprinkler":"TT","Rain":"TT","Wet Grass":"TTT"}
    infer2 = {"Cloudy":"T","Sprinkler":"TT","Rain":"TF","Wet Grass":"TFT"}
    infer3 = {"Cloudy":"T","Sprinkler":"TF","Rain":"TT","Wet Grass":"FTT"}
    infer4 = {"Cloudy":"T","Sprinkler":"TF","Rain":"TF","Wet Grass":"FFT"}
    infer5 = {"Cloudy":"F","Sprinkler":"FT","Rain":"FT","Wet Grass":"TTT"}
    infer6 = {"Cloudy":"F","Sprinkler":"FT","Rain":"FF","Wet Grass":"TFT"}
    infer7 = {"Cloudy":"F","Sprinkler":"FF","Rain":"FT","Wet Grass":"FTT"}
    infer8 = {"Cloudy":"F","Sprinkler":"FF","Rain":"FF","Wet Grass":"FFT"}
    prob = 0.0
    prob += classify_casual(model,infer)
    prob += classify_casual(model,infer2)
    prob += classify_casual(model,infer3)
    prob += classify_casual(model,infer4)
    prob += classify_casual(model,infer5)
    prob += classify_casual(model,infer6)
    prob += classify_casual(model,infer7)
    prob += classify_casual(model,infer8)
    
    print("Inference: ",prob*100,"%")


if __name__ == "__main__":
    main()
    
    
"""
- The probability of the grass being wet, given rain, sprinkler and cloud cover.
- The probability of wet grass given no clouds, no rain and no sprinkler. 
- The probability of wet grass given all variables.
"""
