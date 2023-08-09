import statistics
import unittest

def calculate_statistics(data):
    """
    Calculate mean, median, and standard deviation of a list of numerical data.
    Parameters:
    - data (list): List of numerical data.
    Returns:
    - tuple: (mean, median, standard deviation).
    """
    mean = statistics.mean(data)
    median = statistics.median(data)
    std_dev = statistics.stdev(data)
    return mean, median, std_dev

class TestStatisticsCalculations(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(calculate_statistics([]), (0, 0, 0))

    def test_single_element_list(self):
        self.assertEqual(calculate_statistics([5]), (5, 5, 0))

    def test_positive_values(self):
        data = [10, 20, 30, 40, 50]
        self.assertEqual(calculate_statistics(data), (30, 30, statistics.stdev(data)))

    def test_mixed_values(self):
        data = [-10, 0, 10, 20, 30]
        self.assertEqual(calculate_statistics(data), (10, 10, statistics.stdev(data)))

    def test_negative_values(self):
        data = [-50, -40, -30, -20, -10]
        self.assertEqual(calculate_statistics(data), (-30, -30, statistics.stdev(data)))

unittest.main()
