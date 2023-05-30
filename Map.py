import matplotlib.pyplot as plt

def drawMap(tourmanager, best_path):
    for city in tourmanager:
        plt.plot(city.getX(), city.getY(), "ro")
        plt.annotate(city.getSymbol(), (city.getX(), city.getY()))

    for i in range(len(best_path)):
        try:
            first = best_path[i]
            second = best_path[i + 1]

            plt.plot([first.getX(), second.getX()], [first.getY(), second.getY()], "gray")
        except:
            continue

    first = best_path[0]
    second = best_path[-1]
    plt.plot([first.getX(), second.getX()], [first.getY(), second.getY()], "gray")

    plt.show()