class CityNode:
    def __init__(self, city_name, dist):
        self.city = str(city_name)
        self.dist = int(dist)

def get_romania_map():
    romania = {}
    file = open("romania.txt", 'r')
    for line in file:
        arg = line.split(',')
        city1 = arg[0]
        city2 = arg[1]
        dist = int(arg[2])
        romania.setdefault(city1, []).append(CityNode(city2, dist))
        romania.setdefault(city2, []).append(CityNode(city1, dist))
    return romania

def get_romania_heuristic():
    heuristic = {}
    file = open("romania_sld.txt", 'r')
    for line in file:
        arg = line.split(',')
        city = arg[0]
        value = int(arg[1])
        heuristic[city] = value
    return heuristic