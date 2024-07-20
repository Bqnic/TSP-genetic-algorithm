import numpy as np

#change this array for another case
city_coordinates = [
    np.array([1, 1]),
    np.array([2, 3]),
    np.array([3, 2]),
    np.array([4, 1]),
    np.array([6, 1]),
    np.array([6, 3]),
    np.array([4, 5])
]

def get_cities():
    cities = []
    for city in city_coordinates:
        cities.append(city)

    return cities
