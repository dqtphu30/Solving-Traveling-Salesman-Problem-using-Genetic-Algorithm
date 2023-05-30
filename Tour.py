from City import City
import random
class TourManager:
    destinationCities = []

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.destinationCities):
            result = self.destinationCities[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration
    def add_city(self, city):
        self.destinationCities.append(city)

    def get_city(self, index):
        return self.destinationCities[index]

    def numberOfCities(self):
        return len(self.destinationCities)

    def read_file_tour(self, filename):
        f = open(filename)
        for i in f.readlines():
            node_city_val = i.split()
            symbol, x, y = node_city_val[0], float(node_city_val[1]), float(node_city_val[2])
            self.add_city(City(symbol, x, y))

    def resetTour(self):
        return self.destinationCities.clear()
class Tour:
    def __init__(self, tourmanager, tour=None):
        self.tourmanager = tourmanager
        self.tour = []
        self.fitness = 0.0
        self.distance = 0
        if tour is not None:
            self.tour = tour
        else:
            for i in range(0, self.tourmanager.numberOfCities()):
                self.tour.append(None)

    def __len__(self):
        return len(self.tour)

    def __getitem__(self, index):
        return self.tour[index]

    def __setitem__(self, key, value):
        self.tour[key] = value

    def __repr__(self):
        symbol_list = [city.getSymbol() for city in self.tour]
        answer = ' -> '.join(symbol_list)
        return answer

    def get_city(self, tourPosition):
        return self.tour[tourPosition]

    def set_city(self, tourPosition, city):
        self.tour[tourPosition] = city
        self.fitness = 0.0
        self.distance = 0

    def generate_individual(self):
        for cityIndex in range(0, self.tourmanager.numberOfCities()):
            self.set_city(cityIndex, self.tourmanager.get_city(cityIndex))
        random.shuffle(self.tour)

    def get_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.get_distance())
        return self.fitness

    def get_distance(self):
        if self.distance == 0:
            tourDistance = 0
            for cityIndex in range(0, self.tour_size()):
                fromCity = self.get_city(cityIndex)
                destinationCity = None
                if cityIndex + 1 < self.tour_size():
                    destinationCity = self.get_city(cityIndex + 1)
                else:
                    destinationCity = self.get_city(0)
                tourDistance += fromCity.distanceTo(destinationCity)
            self.distance = tourDistance
        return self.distance

    def tour_size(self):
        return len(self.tour)

    def contains_city(self, city):
        return city in self.tour

    def get_answer(self):
        symbol_list = [city.getSymbol() for city in self.tour]
        answer = ' -> '.join(symbol_list)
        return answer