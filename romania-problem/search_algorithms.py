from priority_queue import PriorityQueue

def dfs(src, dst, romania):
    path = {}
    distance = {}
    pq = PriorityQueue()

    pq.push(src, 0)
    distance[src] = 0
    path[src] = None
    expandedlist = []

    while (pq.is_empty() == False):
        curr = pq.pop()
        if (curr[1] == dst):
            break
        expandedlist.append(curr[1])
        for new in romania[curr[1]]:
            cost = int(curr[0]) + int(new.dist)
            if (new.city not in distance):
                distance[new.city] = cost
                pq.push(new.city, cost)
                path[new.city] = curr[1]
    
    print_path(src, dst, path, distance, expandedlist, "DFS")

def greedy_bfs(src, dst, romania, heuristic):
    path = {}
    distance = {}
    pq = PriorityQueue()

    pq.push(src, 0)
    distance[src] = 0
    path[src] = None
    expandedlist = []

    while (pq.is_empty() == False):
        curr = pq.pop()
        expandedlist.append(curr[1])

        if (curr[1] == dst):
            break

        for new in romania[curr[1]]:
            gcost = distance[curr[1]] + int(new.dist)

            if (new.city not in distance):
                distance[new.city] = gcost
                fcost = heuristic[new.city]
                pq.push(new.city, fcost)
                path[new.city] = curr[1]
    
    print_path(src, dst, path, distance, expandedlist, "Greedy BFS")

def astar(src, dst, romania, heuristic):
    path = {}
    distance = {}
    pq = PriorityQueue()

    pq.push(src, 0)
    distance[src] = 0
    path[src] = None
    expandedlist = []

    while (pq.is_empty() == False):
        curr = pq.pop()
        expandedlist.append(curr[1])

        if (curr[1] == dst):
            break

        for new in romania[curr[1]]:
            gcost = distance[curr[1]] + int(new.dist)

            if (new.city not in distance or gcost < distance[new.city]):
                distance[new.city] = gcost
                fcost = gcost + heuristic[new.city]
                pq.push(new.city, fcost)
                path[new.city] = curr[1]
    
    print_path(src, dst, path, distance, expandedlist, "A Star")

def print_path(src, dst, path, distance, expandedlist, method):
    fixpath = []
    end = dst

    while (path.get(end) != None):
        fixpath.append(end)
        end = path[end]
    fixpath.append(src)
    fixpath.reverse()
    print("Program algoritma " + str(method) + " untuk masalah Romania Arad => Bucharest")
    print("=======================================================")
    print("Kota yg mungkin dijelajah \t\t: " + str(expandedlist))
    print("Jumlah kemungkinan kota \t\t: " + str(len(expandedlist)))
    print("=======================================================")
    print("Kota yg dilewati dg jarak terpendek\t: " + str(fixpath))
    print("Jumlah kota yang dilewati \t\t: " + str(len(fixpath)))
    print("Total jarak \t\t\t\t: " + str(distance[dst]))