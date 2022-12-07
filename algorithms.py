import math

def euclidean_distance(x_1, y_1, x_2, y_2)->float:
    euclidean_Distance = math.sqrt(((x_2-x_1)**2) + ((y_2-y_1)**2))
    return euclidean_Distance
