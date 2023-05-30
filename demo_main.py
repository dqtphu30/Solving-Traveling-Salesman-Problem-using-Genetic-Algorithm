from Map import drawMap
from Tour import TourManager
from Population import Population
from Genetic import Genetic
import time
if __name__ == '__main__':
    tourmanager = TourManager()
    start_time = time.time()
    tourmanager.read_file_tour('TSP42.txt')
    # Initialize population
    pop = Population(tourmanager, 100, True)

    # Evolve population for 50 generations
    ga = Genetic(tourmanager, 1000)
    # pop = ga.evolvePopulation(pop)
    # for i in range(0, 1000):
    #     pop = ga.evolvePopulation(pop)
    best = ga.evolvePopulation(pop)
    end_time = time.time()
    best_path = best.getFittest()
    total_distance = str(best.getFittest().get_distance())
    # Print final results
    print(end_time - start_time)
    print("Initial distance: " + str(pop.getFittest().get_distance()))
    print("Finished")
    print("Final distance: " + total_distance)
    print("Solution:" + '\n' + best_path.get_answer())
    drawMap(tourmanager, best_path)