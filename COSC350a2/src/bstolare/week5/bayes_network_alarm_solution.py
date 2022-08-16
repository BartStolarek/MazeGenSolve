# Discrete Bayesian Network - Algorithm - P 514 on prescribed text
from node import Node

def make_model():
    # Remember that the models do not include false values, you will need to calculate these.
    model = []
    b = Node("Burglary")
    b.add_cpt("t",0.001)
    b.add_cpt("f",0.999)
    
    model.append(b)
    
    e = Node("Earthquake")
    e.add_cpt("t",0.002)
    e.add_cpt("f",0.998)
    
    model.append(e)
    
    a = Node("Alarm")
    a.add_cpt("ttt",0.95)
    a.add_cpt("ttf",0.05)
    a.add_cpt("tft",0.94)
    a.add_cpt("tff",0.06)
    a.add_cpt("ftt",0.29)
    a.add_cpt("ftf",0.71)
    a.add_cpt("fft",0.001)
    a.add_cpt("fff",0.999)
    
    model.append(a)
    b.add_child(a)
    e.add_child(a)
    
    j = Node("JohnCalls")
    j.add_cpt("tt",0.9)
    j.add_cpt("tf",0.1)
    j.add_cpt("ft",0.05)
    j.add_cpt("ff",0.95)
    
    model.append(j)
    a.add_child(j)
    
    m = Node("MaryCalls")
    m.add_cpt("tt",0.7)
    m.add_cpt("tf",0.3)
    m.add_cpt("ft",0.01)
    m.add_cpt("ff",0.99)
    
    model.append(m)
    a.add_child(m)
    
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
    infer = {"Burglary":"t","Earthquake":"t","Alarm":"ttt"}
    infer2 = {"Burglary":"f","Earthquake":"t","Alarm":"ftt"}
    
    
    prob = 0.0
    prob += classify_casual(model,infer)
    prob += classify_casual(model,infer2)
    
    print("Inference: ",prob*100,"%")


if __name__ == "__main__":
    main()
    
    
"""
- The probability that Mary calls given a burglary and alarm.
- The probability that John calls given no alarm and an earthquake.
- The probability of an earth quake given an alarm.
  P(E|A) = P(E) * P(B) * P(A|E,B) + P(E) * P(-B) * P(A|E,-B) 
"""

