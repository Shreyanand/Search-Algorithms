graph = {'A': ['D','B'],
         'B': ['C'],
         'C': ['G','D'],
         'D': ['G'],
         'G': []
        }
Weights = {}
Weights[('A','B')] = 1.0
Weights[('B','C')] = 2.0
Weights[('C','G')] = 4.0
Weights[('D','G')] = 2.0
Weights[('A','D')] = 5.0
Weights[('C','D')] = 1.0

def mi(Q):
    item =  min(Q, key = lambda x: x[0]) 
    Q.remove(item)
    return item

def uniform(graph,source,goal):
    if source == goal:
        return [source,goal]
    q = []
    explored = {}
    node  = 0
    q.append((0,[source]))
    exploreList = []
    
    while q:
        print q
        var = mi(q)
        path = var[1]
        pathcost = var[0]
        node = path[len(path) - 1]
        explored[node] = [pathcost, path] 
        if node == goal:
            for key in explored:
                exploreList.append(key)
            # print exploreList
            # print len(exploreList)
            # print explored[node][1]  
            # print len(explored[node][1])
            return explored
            #print "A total of "+ str(len(explored)) + " nodes were visited using astar: " + str(explored)
            #return path 
        for v in graph[node]:

            UpdatedPath = path[:]
            UpdatedPath.append(v)
            Vpathcost = pathcost + Weights[node,v]
            f = Vpathcost
            #if v == "G": print explored
            if v not in explored:
                for i in q:
                    if i[1][-1] == v:
                        q.remove(i)
                q.append((f,UpdatedPath))               
            else:
                q.append((f,UpdatedPath))        
            
                              
    return "Not found"
print uniform(graph,'A','G')