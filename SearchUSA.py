#######################################Parsing the file####################################################
import sys
Algorithm = sys.argv[1]
Source_city = sys.argv[2]
Destination_city = sys.argv[3] 

import math
plfile = open('usroads.pl') #####Please update this path 
edge = []
coordinate = {} 
count = 0
for i in range(0,5):
    plfile.next()
for i in plfile:
    i = i.replace(".","\n").split("\n")
    if i == ['%==============================================================================', '']:
        break
    else:
        for ele in i:
            if ele != '':
                edge.append(ele.replace(" ","").replace(")","").replace("(","")[4:].split())

for i in range(0,25):
    plfile.next()                
for i in plfile:
    i = i.split("\n")

    for ele in i:
        if ele != '':
            var = ele.replace(" ","").replace(").","").replace("(","")[4:].split(",")
            coordinate[var[0]] = [float(var[1]),float(var[2])]
            

# XY = {}
# for i in coordinate:
#     splitted = i.split(",")
#     XY[splitted[0]] = [splitted[1],splitted[2]] 

###########################################Cnstructing the Graph######################################

Graph = {}
Weights = {}
def addEdge(Graph,I,F,W):
    if I in Graph:
        Graph[I].append(F)
    else:
        Graph[I] = [F]
    Weights[(I,F)] = float(W)

for i in edge:
    splitted = i[0].split(",")
    addEdge(Graph,splitted[0],splitted[1],splitted[2])
    addEdge(Graph,splitted[1],splitted[0],splitted[2])
    
def pathcost(path):
    cost = 0
    for i in range(0,len(path) - 1):
        cost += Weights[(path[i], path[i+1])]
    return cost

##################Heuristic Function #############################################    
def heuristic(City1, City2):
    Lat1 = coordinate[City1][0]
    Lat2 = coordinate[City2][0]
    Long1 = coordinate[City1][1]
    Long2 = coordinate[City2][1]
    return math.sqrt((69.5 * (Lat1 - Lat2)) ** 2 + (69.5 * math.cos((Lat1 + Lat2)/360 * math.pi) * (Long1 - Long2)) ** 2)
    
 #########################Algorithms###############################################
def mi(Q):
    item =  min(Q, key = lambda x: x[0]) 
    Q.remove(item)
    return item
    
def astar(graph,source,goal):
    q = []
    explored = {}
    exploreList = []
    node  = 0
    q.append((heuristic(source,goal),[source],0))

    while q:
        var = mi(q)
        path = var[1]
        pathcost = var[2]
        node = path[len(path) - 1]
        explored[node] = [pathcost, path] 
        if node == goal:
            for key in explored:
                exploreList.append(key)
            print exploreList
            print len(exploreList)
            print explored[node][1]  
            print len(explored[node][1])
            return explored[node][0]

        for v in graph[node]:

            UpdatedPath = path[:]
            UpdatedPath.append(v)
            Vpathcost = pathcost + Weights[node,v]
            f = Vpathcost + heuristic(v,goal)
            if v in explored:
                if f < explored[v][0]:
                    explored[v] = [f, UpdatedPath]
                    for i in q:
                        if i[1][-1] == v:
                            q.remove(i)
                    q.append((f,UpdatedPath,Vpathcost))               
            else:
                q.append((f,UpdatedPath,Vpathcost))        
            
                              
    return "Not found"

def greedy(graph,source,goal):
    q = []
    node  = 0
    explored = []
    q.append((heuristic(source,goal),[source]))

    while q:
        var = mi(q)
        path = var[1]
        node = path[len(path) - 1]
        explored.append(node)
        if node == goal:
            print explored
            print len(explored)
            print path 
            print len(path)
            return pathcost(path)
        for v in graph[node]:
            if v not in explored:
                UpdatedPath = path[:]
                UpdatedPath.append(v)
                f = heuristic(v,goal)
                q.append((f,UpdatedPath))        
            
                              
    return "Not found"    
    
def uniform(graph,source,goal):
    q = []
    explored = {}
    node  = 0
    q.append((0,[source]))
    exploreList = []
    while q:
        var = mi(q)
        path = var[1]
        pathcost = var[0]
        node = path[len(path) - 1]
        explored[node] = [pathcost, path] 
        if node == goal:
            for key in explored:
                exploreList.append(key)
            print exploreList
            print len(exploreList)
            print explored[node][1]  
            print len(explored[node][1])
            return explored[node][0]
        for v in graph[node]:

            UpdatedPath = path[:]
            UpdatedPath.append(v)
            Vpathcost = pathcost + Weights[node,v]
            f = Vpathcost
            if v in explored:
                if f < explored[v][0]:
                    explored[v] = [f, UpdatedPath]
                    for i in q:
                        if i[1][-1] == v:
                            q.remove(i)
                    q.append((f,UpdatedPath))               
            else:
                q.append((f,UpdatedPath))        
            
                              
    return "Not found"

        
                    
# print astar(Graph, 'boston', 'omaha')
# print astar(Graph, 'omaha', 'boston')
# print astar(Graph, 'sanDiego', 'boston')
# #print greedy(Graph, 'montreal', 'newYork')
# #print greedy(Graph, 'sanDiego', 'boston')
# #print uniform(Graph, 'miami', 'vancouver')
# print uniform(Graph, 'sanDiego', 'boston')
if Algorithm == 'astar':
    print astar(Graph,Source_city,Destination_city)
elif Algorithm == 'greedy':
    print greedy(Graph,Source_city,Destination_city)
elif Algorithm == 'uniform':
    print uniform(Graph,Source_city,Destination_city)
