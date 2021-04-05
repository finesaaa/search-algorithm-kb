from priority_queue import PriorityQueue

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
        expandedlist.append(curr)

        if (curr == dst):
            break

        for new in romania[curr]:
            gcost = distance[curr] + int(new.dist)

            if (new.city not in distance):
                distance[new.city] = gcost
                fcost = heuristic[new.city]
                pq.push(new.city, fcost)
                path[new.city] = curr
    
    print_path(src, dst, path, distance, expandedlist)

def print_path(src, dst, path, distance, expandedlist):
    fixpath = []
    end = dst

    while (path.get(end) != None):
        fixpath.append(end)
        end = path[end]
    fixpath.append(src)
    fixpath.reverse()
    print("Program algoritma Astar untuk masalah Romania\tArad => Bucharest")
    print("=======================================================")
    print("Kota yg mungkin dijelajah \t\t: " + str(expandedlist))
    print("Jumlah kemungkinan kota \t\t: " + str(len(expandedlist)))
    print("=======================================================")
    print("Kota yg dilewati dg jarak terpendek\t: " + str(fixpath))
    print("Jumlah kota yang dilewati \t\t: " + str(len(fixpath)))
    print("Total jarak \t\t\t\t: " + str(distance[dst]))