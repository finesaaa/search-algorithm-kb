import heapq

class PriorityQueue: 
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)

    def is_empty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)