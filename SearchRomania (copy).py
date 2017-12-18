# Code by SHREY ANAND

# plfile = open('/home/shrey/Desktop/roads.pl')
# remove_head = plfile.next().rstrip()
# for i in plfile:
#     print i
 
# import sys
# Algorithm = sys.argv[1]
# Source_city = sys.argv[2]
# Destination_city = sys.argv[3] 

graph = {'oradea': ['sibiu','zerind'],
         'sibiu': ['arad','fagaras','oradea', 'rimnicu_vilcea'],
         'zerind': ['arad', 'oradea'],
         'arad': ['sibiu', 'timisoara','zerind'],
         'fagaras': ['bucharest', 'sibiu'],
         'rimnicu_vilcea': ['craiova', 'pitesti','sibiu'],
         'timisoara': ['arad','lugoj'],
         'bucharest' : ['fagaras', 'giurgiu', 'pitesti', 'urziceni'],
         'craiova' : ['dobreta','pitesti','rimnicu_vilcea'],
         'pitesti' : ['bucharest','craiova','rimnicu_vilcea'],
         'lugoj' : ['mehadia','timisoara'],
         'giurgiu' : ['bucharest'],
         'urziceni' : ['bucharest','hirsova','vaslui'],
         'dobreta' : ['craiova','mehadia'],
         'hirsova' : ['eforie','urziceni'],
         'vaslui' : ['iasi','urziceni'],
         'iasi' : ['neamt','vaslui'],
         'eforie' : ['hirsova'],
         'neamt' : ['iasi'],
         'mehadia': ['dobreta','lugoj']
         }
         

         
def BFS(graph,source,goal):
    if source == goal:
        return [source,goal]
    frontier = []
    explored = []
    node  = 0
    frontier.append([source])
#    explored.append(source)
    while frontier:
        #print frontier
        path = frontier.pop(0)
        node = path[len(path) - 1]
        explored.append(node) #here if want to see node expanded but if you don't have a different list for visited nodes then sometimes while visted nodes wait to be explored they will be visted again. So technically we should check visted nodes before adding to frontier. 
        #print frontier
        for v in graph[node]:
            if v not in explored:
                UpdatedPath = path[:]
                UpdatedPath.append(v)
#                explored.append(v) Here if want to know visted
                if v == goal:
                    print "A total of "+ str(len(explored)) + " nodes were visited using BFS: " + str(explored)
                    return UpdatedPath
                frontier.append(UpdatedPath)
                
    return "Not found"
     
print "Final BFS path: " + str( BFS(graph,'dobreta', 'fagaras'))
#print "Final BFS path: " + str( BFS(graph,'dobreta', 'fagaras'))
   


mystack = []        
seen = []

def DFS(graph,source,goal):
    if goal == source:
        return [source,goal]
    else:
        path = [source]
        mystack.append(path)
        val  = DFS_visit(graph,path,goal)
        return val
    

def DFS_visit(graph,path,goal):   
    while mystack:
        #print mystack
        path = mystack.pop()
        node = path[-1]
        #print node
        seen.append(node)
        #print seen
        for v in reversed(graph[node]):
            if v not in seen:
                #print path
                #print v
                UpdatedPath = path[:]
                UpdatedPath.append(v)
                if v == goal:
                    print "A total of "+ str(len(seen)) + " nodes were visited using DFS: " + str(seen)       
                    seen[:] = []
                    return UpdatedPath
                else:
                    #print UpdatedPath
                    mystack.append(UpdatedPath)
                    #return DFS_visit(graph,UpdatedPath,goal)
        

#print "Final DFS path: " + str(DFS(graph,'fagaras', 'dobreta'))
#print "Final DFS path: " + str(DFS(graph,'dobreta','fagaras'))         

# if Algorithm == 'BFS':
#     print "Final BFS path: " + str(BFS(graph,Source_city,Destination_city))
# elif Algorithm == 'DFS':
#     print "Final DFS path: " + str(DFS(graph,Source_city,Destination_city))

###############VERIFICATION FOR 4b and 4c ###########################################
                                    
# for keyS in graph:
#     for keyD in graph: 
#         if BFS(graph,keyS,keyD) < DFS(graph,keyS,keyD):
#             print keyS +" " + keyD   
        
    