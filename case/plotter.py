import matplotlib.pyplot as plt
import city_positions

cities = city_positions.get_cities()

for city in cities:
    plt.plot(city[0], city[1], 'o')
plt.show()