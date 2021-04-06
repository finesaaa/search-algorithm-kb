from priority_queue import PriorityQueue
from typing import Dict, List, Any
import time

def dfs(src: str, dst: str, romania: Dict[str, Any], visited: List[str], path: Dict[str, str],
        distance: int, depth_limit: int = 100, depth: int = 0) -> bool:
    if (src == dst):
        print_result("Arad", dst, path, {dst: distance}, "DFS")
        return True
    
    if (depth >= depth_limit):
        return False

    visited.append(src)

    for node in romania[src]:
        if (node.city not in visited):
            path[node.city] = src
            if (dfs(node.city, dst, romania, visited, path, distance + node.dist, depth_limit,
                depth + 1)):
                return True

    return False


def ids(src: str, dst: str, romania: Dict[str, Any]):
    for depth in range(1, len(romania)):
        if (dfs(src, dst, romania, [], {}, 0, depth)):
            break


def greedy_bfs(src: str, dst: str, romania: Dict[str, Any], heuristic: Dict[str, int]):
    path = {}
    distance = {}
    openList = PriorityQueue()
    closedList = []
    
    openList.push(src, 0)
    distance[src] = 0
    path[src] = None

    while (openList.is_empty() == False):
        curr = openList.pop()
        closedList.append(curr[1])

        if (curr[1] == dst):
            break

        for node in romania[curr[1]]:
            gcost = distance[curr[1]] + int(node.dist)

            if (node.city not in distance):
                distance[node.city] = gcost
                fcost = heuristic[node.city]
                openList.push(node.city, fcost)
                path[node.city] = curr[1]
    
    print_result(src, dst, path, distance, "Greedy BFS")


def astar(src, dst, romania, heuristic):
    path = {}
    distance = {}
    openList = PriorityQueue()
    closedList = []
    
    openList.push(src, 0)
    distance[src] = 0
    path[src] = None

    while (openList.is_empty() == False):
        curr = openList.pop()
        closedList.append(curr[1])

        if (curr[1] == dst):
            break

        for node in romania[curr[1]]:
            gcost = distance[curr[1]] + int(node.dist)

            if (node.city not in distance or gcost < distance[node.city]):
                distance[node.city] = gcost
                fcost = gcost + heuristic[node.city]
                openList.push(node.city, fcost)
                path[node.city] = curr[1]
    
    print_result(src, dst, path, distance, "A Star")


def print_result(src: str, dst: str, path: Dict[str, Any], distance: Dict[str, int], method: str):
    new_path = []
    target = dst

    while (path.get(target) != None):
        new_path.append(target)
        target = path[target]

    new_path.append(src)
    new_path.reverse()

    print("Penyelesaian masalah Romania Arad => Bucharest menggunakan algoritma " + method)
    print("=======================================================================")
    print("Kota yg dilewati\t: " + str(new_path))
    print("Jumlah kota\t\t: " + str(len(new_path)))
    print("Total jarak\t\t: " + str(distance[dst]))