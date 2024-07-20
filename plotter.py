import matplotlib.pyplot as plt
from case.city_positions import get_cities

cities = get_cities()

for city in cities:
    plt.plot(city[0], city[1], 'o')

for i, (x1, y1) in enumerate(cities):
    for j, (x2, y2) in enumerate(cities):
        if i < j:  
            plt.plot([x1, x2], [y1, y2], color='gray', linestyle='-', linewidth=0.5)

plt.show()
