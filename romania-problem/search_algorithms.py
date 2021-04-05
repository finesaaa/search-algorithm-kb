from priority_queue import PriorityQueue
from typing import Dict, List, Any

def dfs(src: str, dst: str, romania: Dict[str, Any], visited: List[str], path: Dict[str, str], distance: int, depth_limit: int = 100, depth: int = 0) -> bool:
    if (src == dst):
        print_path(src, dst, path, {dst: distance}, visited, "DFS")
        return True
    
    if (depth >= depth_limit):
        return False

    visited.append(src)

    for item in romania[src]:
        if (item.city not in visited):
            path[item.city] = src
            if (dfs(item.city, dst, romania, visited, path, distance + item.dist, depth_limit, depth + 1)):
                return True

    return False

def ids(src: str, dst: str, romania: Dict[str, Any]):
    for depth in range(1, len(romania)):
        if (dfs(src, dst, romania, [], {}, 0, depth)):
            break

def greedy_bfs(src: str, dst: str, romania: Dict[str, Any], heuristic: Dict[str, int]):
    path = {}
    distance = {}
    pq = PriorityQueue()

    pq.push(src, 0)
    distance[src] = 0
    path[src] = None
    closedList = []

    while (pq.is_empty() == False):
        curr = pq.pop()
        closedList.append(curr[1])

        if (curr[1] == dst):
            break

        for new in romania[curr[1]]:
            gcost = distance[curr[1]] + int(new.dist)

            if (new.city not in distance):
                distance[new.city] = gcost
                fcost = heuristic[new.city]
                pq.push(new.city, fcost)
                path[new.city] = curr[1]
    
    print_path(src, dst, path, distance, closedList, "Greedy BFS")

def astar(src, dst, romania, heuristic):
    path = {}
    distance = {}
    pq = PriorityQueue()

    pq.push(src, 0)
    distance[src] = 0
    path[src] = None
    closedList = []

    while (pq.is_empty() == False):
        curr = pq.pop()
        closedList.append(curr[1])

        if (curr[1] == dst):
            break

        for new in romania[curr[1]]:
            gcost = distance[curr[1]] + int(new.dist)

            if (new.city not in distance or gcost < distance[new.city]):
                distance[new.city] = gcost
                fcost = gcost + heuristic[new.city]
                pq.push(new.city, fcost)
                path[new.city] = curr[1]
    
    print_path(src, dst, path, distance, closedList, "A Star")

def print_path(src: str, dst: str, path: Dict[str, Any], distance: Dict[str, int], closedList: List[str], method: str):
    fixpath = []
    end = dst

    while (path.get(end) != None):
        fixpath.append(end)
        end = path[end]
    fixpath.append(src)
    fixpath.reverse()

    print("Program algoritma " + method + " untuk masalah Romania Arad => Bucharest")
    print("=======================================================")
    print("Kota yg mungkin dijelajah \t\t: " + str(closedList))
    print("Jumlah kemungkinan kota \t\t: " + str(len(closedList)))
    print("=======================================================")
    print("Kota yg dilewati dg jarak terpendek\t: " + str(fixpath))
    print("Jumlah kota yang dilewati \t\t: " + str(len(fixpath)))
    print("Total jarak \t\t\t\t: " + str(distance[dst]))