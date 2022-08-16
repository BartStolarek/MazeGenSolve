

# Adjacency list
map_graph = {'Arad':['Zerind','Sibiu','Timisoara'],
             'Bucharest':['Urziceni','Giurgiu','Fagaras','Pitesti'],
             'Craiova':['Pitesti','Rimnicu Vilcea','Craiova'],
             'Dobreta':['Mehadia','Craiova'],
             'Eforie':['Hirsova'],
             'Fagaras':['Sibiu','Bucharest'],
             'Giurgiu':['Bucharest'],
             'Hirsova':['Eforie','Urziceni'],
             'Iasi':['Neamt','Vaslui'],
             'Lugoj':['Timisoara','Mehadia'],
             'Mehadia':['Lugoj','Dobreta'],
             'Neamt':['Iasi'],
             'Oradea': ['Zerind','Sibiu'],
             'Pitesti':['Rimnicu Vilcea','Craiova','Bucharest'],
             'Rimnicu Vilcea':['Sibiu','Craiova','Pitesti'],
             'Sibiu':['Oradea','Arad','Fagaras','Rimnicu Vilcea'],
             'Timisoara':['Arad','Lugoj'],
             'Urziceni':['Bucharest','Hirsova','Vaslui'],
             'Vaslui':['Iasi','Urziceni'],
             'Zerind':['Oradea','Arad'] } 


heuristic_cost = {'Arad': 366,
                'Bucharest': 0,
                'Craiova': 160,
                'Dobreta': 242,
                'Eforie': 161,
                'Fagaras': 176,
                'Giurgiu': 77,
                'Hirsova': 151,
                'Iasi': 226,
                'Lugoj': 244,
                'Mehadia': 241,
                'Neamt': 234,
                'Oradea': 380,
                'Pitesti': 100,
                'Rimnicu Vilcea': 193,
                'Sibiu': 253,
                'Timisoara': 329,
                'Urziceni': 80,
                'Vaslui': 199,
                'Zerind': 374}

cost_map = {('Arad', 'Zerind'): 75,
            ('Arad', 'Sibiu'): 140,
            ('Arad', 'Timisoara'): 118,
            ('Oradea','Zerind'): 71,
            ('Oradea', 'Sibiu'): 151,
            ('Lugoj','Timisoara'): 111,
            ('Fagaras','Sibiu'): 99,
            ('Rimnicu Vilcea','Sibiu'): 80,
            ('Lugoj', 'Mehadia'): 70,
            ('Bucharest','Fagaras'): 211,
            ('Pitesti','Rimnicu Vilcea'): 97,
            ('Craiova','Rimnicu Vilcea'): 146,
            ('Dobreta','Mehadia'): 75,
            ('Bucharest', 'Pitesti'): 101,
            ('Bucharest', 'Urziceni'): 85,
            ('Bucharest', 'Giurglu'): 90,
            ('Craiova', 'Pitesti'): 138,
            ('Craiova', 'Dobreta'): 120,
            ('Hirsova', 'Urziceni'): 98,
            ('Urziceni', 'Vaslui'): 142,
            ('Eforie', 'Hirsova'): 86,
            ('Lasi', 'Vaslui'): 92,
            ('Lasi', 'Neamt'): 87}

def sort_q(queue):
    # key is set to sort using second element of 
    # sublist lambda has been used
    queue.sort(key = lambda x: x[1])
    return queue

def get_cost(key_tuple):
    return cost_map[ tuple(sorted(key_tuple)) ]

def a_star(graph,start,goal):
    queue = []
    queue.append([start,0])
    visited = []
    
    cost_so_far = {}
    cost_so_far[start] = 0
    came_from = {}
    came_from[start] = start
    
    while queue:
        parent = queue.pop(0)
        if parent[0] == goal:
            break
        for child in graph[parent[0]]:
            new_cost = cost_so_far[parent[0]] + get_cost((child,parent[0]))
            if child not in cost_so_far or new_cost < cost_so_far[child]:
                cost_so_far[child] = new_cost
                priority = new_cost + heuristic_cost[child]
                #print([child,priority])
                queue.append([child,priority])
                came_from[child] = parent[0]
        sort_q(queue)
    
    print(came_from)
    current = goal
    while current != start:
        visited.append(current)
        current = came_from[current]
    visited.append(start)
    visited.reverse()
    
    return visited
                

def main():
    global map_graph
    #if tuple(sorted(('Zerind','Arad'))) in cost_map:
    #   print( get_cost(('Zerind','Arad')) )
    visited = a_star(map_graph,'Arad','Bucharest') 
    print(visited)


if __name__ == "__main__":
    main()
