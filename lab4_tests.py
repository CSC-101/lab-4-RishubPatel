import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = [[], [0], [12,3,45,6]]
        result = lab4.first_element(input)
        expected = [0, 12]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coord_1(self):
        point1 = data.Point(5, 5)
        point2 = data.Point(7, -3)
        input = [point1, point2]
        result = lab4.x_coordinates(input)
        expected = [5, 7]
        self.assertEqual(expected, result)

    def test_x_coord_2(self):
        point1 = data.Point(0, 0)
        point2 = data.Point(-1, 4)
        input = [point1, point2]
        result = lab4.x_coordinates(input)
        expected = [0, -1]
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant_1(self):
        point1 = data.Point(0, 0)
        point2 = data.Point(-1, 4)
        input = [point1, point2]
        result = lab4.are_in_positive_quadrant(input)
        expected = []
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        point1 = data.Point(4, 6)
        point2 = data.Point(-1, 4)
        input = [point1, point2]
        result = lab4.are_in_positive_quadrant(input)
        expected = [point1]
        self.assertEqual(expected, result)

    # Part 4

    def test_distance_1(self):
        point1 = data.Point(4, 6)
        point2 = data.Point(-1, 4)
        result = lab4.distance(point1, point2)
        expected = 29 ** 0.5
        self.assertEqual(expected, result)

    def test_distance_2(self):
        point1 = data.Point(0, 0)
        point2 = data.Point(7, -3)
        result = lab4.distance(point1, point2)
        expected = 58 ** 0.5
        self.assertEqual(expected, result)

    # Part 5

    def test_manhattan_distance_1(self):
        point1 = data.Point(0, 0)
        point2 = data.Point(7, -3)
        result = lab4.manhattan_distance(point1, point2)
        expected = 10
        self.assertEqual(expected, result)

    def test_manhattan_distance_2(self):
        point1 = data.Point(4, 6)
        point2 = data.Point(4, -1)
        result = lab4.manhattan_distance(point1, point2)
        expected = 7
        self.assertEqual(expected, result)

    # Part 6

    def test_distance_all_1(self):
        points = [data.Point(1, 1), data.Point(5, 1), data.Point(0, 0)]
        self.assertEqual([2**0.5, 26**0.5, 0], lab4.distance_all(points))

    def test_distance_all_2(self):
        points = [data.Point(-1, 1), data.Point(0, 1)]
        self.assertEqual([2**0.5, 1], lab4.distance_all(points))

if __name__ == '__main__':
    unittest.main()
