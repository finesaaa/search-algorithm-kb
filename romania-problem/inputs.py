from typing import Dict, Any
class City:

    def __init__(self, city_name, dist):
        self.city = str(city_name)
        self.dist = int(dist)


def get_romania_map() -> Dict[str, Any]:
    romania = {}
    file = open("romania.txt", 'r')

    for line in file:
        arg = line.split(',')
        city1 = arg[0]
        city2 = arg[1]
        dist = int(arg[2])
        romania.setdefault(city1, []).append(City(city2, dist))
        romania.setdefault(city2, []).append(City(city1, dist))

    return romania


def get_romania_heuristic() -> Dict[str, int]:
    heuristic = {}
    file = open("romania_sld.txt", 'r')

    for line in file:
        arg = line.split(',')
        city = arg[0]
        value = int(arg[1])
        heuristic[city] = value
    
    return heuristic