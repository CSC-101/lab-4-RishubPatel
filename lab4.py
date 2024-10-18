import data

# Write your functions for each part in the space below.

# Part 1

def first_element(big_list:list[list[int]]) -> list: #returns first value of each integer list within big_list
    return [int_list[0] for int_list in big_list if int_list != []]

# Part 2

def x_coordinates(point_list:list[data.Point]) -> list: #lists the x-coordinates for each point in point_list
    return [point.x for point in point_list]

# Part 3

def are_in_positive_quadrant(point_list:list[data.Point]) -> list: #returns all points in first quadrant from point_list
    return [point for point in point_list if point.x > 0 and point.y > 0]

# Part 4

def distance(point_1:data.Point, point_2:data.Point) -> float: #returns distance btwn 2 points
    return (((point_2.x - point_1.x) ** 2) + ((point_2.y - point_1.y) ** 2)) ** 0.5

# Part 5

def manhattan_distance(point1:data.Point, point2:data.Point) -> float: #returns manhattan distance btwn 2 points
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

# Part 6

def distance_all(points:list[data.Point]) -> list: #returns distance from origin of points in points
    origin = data.Point(0, 0)
    return [distance(origin, point) for point in points]