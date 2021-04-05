import heapq

romania = {}

class PriorityQueue: 
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))
    
    def pop(self):
        return heapq.heappop(self.cities)[1]

    def is_empty(self):
        if (self.cities == []):
            return True
        else:
            return False
    
    def check(self):
        print(self.cities)
 
class CityNode:
    def __init__(self, city_name, dist):
        self.city = str(city_name)
        self.dist = int(dist)

def make_dict():
    file = open("romania.txt", 'r')
    for line in file:
        arg = line.split(',')
        city1 = arg[0]
        city2 = arg[1]
        dist = int(arg[2])
        romania.setdefault(city1, []).append(CityNode(city2, dist))
        romania.setdefault(city2, []).append(CityNode(city1, dist))

def make_heuristic_dict():
    heu = {}
    with open("romania_sld.txt", 'r') as file:
        for line in file:
            arg = line.strip().split(',')
            city = arg[0].strip()
            value = int(arg[1].strip())
            heu[city] = value
    return heu

def heuristic(city, heu):
    return heu[city]

def astar(src, dst):
    path = {}
    distance = {}
    pq = PriorityQueue()
    h =  make_heuristic_dict()

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

            if (new.city not in distance or gcost < distance[new.city]):
                distance[new.city] = gcost
                fcost = gcost + h[new.city]
                pq.push(new.city, fcost)
                path[new.city] = curr
    
    print_path(src, dst, path, distance, expandedlist)


def print_path(src, dst, path, distance, expandedlist):
    fixpath = []
    end = dst

    while (path.get(end) != None):
        fixpath.append(end)
        end = path[end]
    finalpath.append(src)
    finalpath.reverse()
    print("Program algoritma Astar untuk masalah Romania")
    print("\tArad => Bucharest")
    print("=======================================================")
    print("Kota yg mungkin dijelajah \t\t: " + str(expandedlist))
    print("Jumlah kemungkinan kota \t\t: " + str(len(expandedlist)))
    print("=======================================================")
    print("Kota yg dilewati dg jarak terpendek\t: " + str(finalpath))
    print("Jumlah kota yang dilewati \t\t\t: " + str(len(finalpath)))
    print("Total jarak \t\t\t\t\t\t: " + str(distance[dst]))

def main():
    src = "Arad"
    dst = "Bucharest"
    make_dict()
    astar(src, dst)

if __name__ == "__main__":
    main()