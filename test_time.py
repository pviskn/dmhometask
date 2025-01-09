import time
from main import Graph
import unittest
import random


class MeasureGraphTime(unittest.TestCase):

    def test_measure_undirected_graph_with_5_vertices(self):
        """
            Тест измерения времени для неориентированного графа с 5 вершинами.
        """
        # given
        g = Graph(5)

        # when
        start_time = time.perf_counter()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 0)
        g.add_edge(1, 4)
        result = g.greedy_coloring()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)

    def test_measure_directed_graph_with_5_vertices(self):
        """
            Тест измерения времени для ориентированного графа с 5 вершинами.
        """
        # given
        g = Graph(5)

        # when
        start_time = time.perf_counter()
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        g.add_edge(2, 3, directed=True)
        g.add_edge(3, 4, directed=True)
        g.add_edge(4, 0, directed=True)
        g.add_edge(1, 4, directed=True)
        result = g.greedy_coloring_directed()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)

    def test_measure_graph_10_vertices_without_edges(self):
        """
            Тест измерения времени для графа с 10 изолированными вершинами.
        """
        # given
        g = Graph(10)

        # when
        start_time = time.perf_counter()
        result = g.greedy_coloring()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)

    def test_measure_undirected_graph_10_vertices_with_edge(self):
        """
            Тест измерения времени для неориентированного графа с 10 вершинами и 1 ребром.
        """
        # given
        g = Graph(10)

        # when
        start_time = time.perf_counter()
        g.add_edge(0, 1)
        result = g.greedy_coloring()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)

    def test_measure_directed_graph_big_number_vertices_with_edge(self):
        """
            Тест измерения времени для ориентированного графа с 10 вершинами и 1 ребром.
        """
        # given
        g = Graph(10)

        # when
        start_time = time.perf_counter()
        g.add_edge(0, 1, directed=True)
        result = g.greedy_coloring_directed()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)

    def test_measure_undirected_graph_10_vertices_with_edges(self):
        """
            Тест измерения времени для неориентированного графа с 10 вершинами.
        """
        # given
        g = Graph(10)

        # when
        start_time = time.perf_counter()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(0, 4)
        g.add_edge(0, 5)
        g.add_edge(0, 6)
        g.add_edge(0, 7)
        g.add_edge(0, 8)
        g.add_edge(0, 9)
        result = g.greedy_coloring()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)

    def test_measure_directed_graph_10_vertices_with_edges(self):
        """
            Тест измерения времени для ориентированного графа с 10 вершинами.
        """
        # given
        g = Graph(10)

        # when
        start_time = time.perf_counter()
        g.add_edge(0, 1, directed=True)
        g.add_edge(0, 2, directed=True)
        g.add_edge(0, 3, directed=True)
        g.add_edge(0, 4, directed=True)
        g.add_edge(0, 5, directed=True)
        g.add_edge(0, 6, directed=True)
        g.add_edge(0, 7, directed=True)
        g.add_edge(0, 8, directed=True)
        g.add_edge(0, 9, directed=True)
        result = g.greedy_coloring_directed()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)

    def test_measure_directed_graph_20_vertices_with_edges(self):
        """
            Тест измерения времени для ориентированного графа с 20 вершинами.
        """
        # given
        g = Graph(20)

        # when
        start_time = time.perf_counter()
        g.add_edge(0, 1, directed=True)
        g.add_edge(0, 2, directed=True)
        g.add_edge(0, 3, directed=True)
        g.add_edge(11, 2, directed=True)
        g.add_edge(11, 2, directed=True)
        g.add_edge(12, 5, directed=True)
        g.add_edge(13, 7, directed=True)
        g.add_edge(18, 9, directed=True)
        g.add_edge(19, 4, directed=True)
        g.add_edge(1, 16, directed=True)
        g.add_edge(4, 4, directed=True)
        g.add_edge(0, 5, directed=True)
        g.add_edge(0, 6, directed=True)
        g.add_edge(0, 7, directed=True)
        g.add_edge(0, 8, directed=True)
        g.add_edge(0, 9, directed=True)
        result = g.greedy_coloring_directed()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)

    def test_measure_undirected_graph_20_vertices_with_edges(self):
        """
            Тест измерения времени для неориентированного графа с 20 вершинами.
        """
        # given
        g = Graph(20)

        # when
        start_time = time.perf_counter()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(11, 2)
        g.add_edge(11, 2)
        g.add_edge(12, 5)
        g.add_edge(13, 7)
        g.add_edge(18, 9)
        g.add_edge(19, 4)
        g.add_edge(1, 16)
        g.add_edge(4, 4)
        g.add_edge(0, 5)
        g.add_edge(0, 6)
        g.add_edge(0, 7)
        g.add_edge(0, 8)
        g.add_edge(0, 9)
        result = g.greedy_coloring()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)

    def test_measure_cycle_graph_big_number_vertices(self):
        """
            Тест измерения времени для циклического графа с 20 вершинами.
        """
        # given
        g = Graph(20)

        # when
        start_time = time.perf_counter()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 6)
        g.add_edge(6, 7)
        g.add_edge(7, 8)
        g.add_edge(8, 9)
        g.add_edge(9, 10)
        g.add_edge(10, 11)
        g.add_edge(11, 12)
        g.add_edge(12, 13)
        g.add_edge(13, 14)
        g.add_edge(14, 15)
        g.add_edge(16, 17)
        g.add_edge(17, 18)
        g.add_edge(18, 19)
        g.add_edge(19, 0)
        result = g.greedy_coloring()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)

    def test_measure_undirected_graph_40_vertices(self):
        """
            Тест измерения времени для неориентированного графа с 40 вершинами.
        """
        # given
        g = Graph(40)

        # when
        start_time = time.perf_counter()
        g.add_edge(39, 39)
        g.add_edge(28, 31)
        g.add_edge(32, 22)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 6)
        g.add_edge(6, 7)
        g.add_edge(7, 8)
        g.add_edge(8, 9)
        g.add_edge(9, 10)
        g.add_edge(9, 14)
        g.add_edge(9, 19)
        g.add_edge(9, 11)
        g.add_edge(10, 11)
        g.add_edge(11, 12)
        g.add_edge(12, 13)
        g.add_edge(13, 14)
        g.add_edge(14, 15)
        g.add_edge(16, 17)
        g.add_edge(17, 18)
        g.add_edge(18, 19)
        g.add_edge(10, 10)
        g.add_edge(19, 0)
        result = g.greedy_coloring()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)

    def test_measure_undirected_graph_60_vertices(self):
        """
            Тест измерения времени для неориентированного графа с 60 вершинами.
        """
        # given
        g = Graph(60)

        # when
        start_time = time.perf_counter()
        g.add_edge(10, 10)
        g.add_edge(19, 0)
        g.add_edge(19, 39)
        g.add_edge(19, 50)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(3, 5)
        g.add_edge(3, 6)
        g.add_edge(19, 7)
        g.add_edge(19, 8)
        g.add_edge(19, 9)
        result = g.greedy_coloring()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)

    def test_measure_undirected_graph_80_vertices(self):
        """
            Тест измерения времени для неориентированного графа с 80 вершинами.
        """
        # given
        g = Graph(80)

        # when
        start_time = time.perf_counter()
        g.add_edge(70, 10)
        g.add_edge(10, 10)
        g.add_edge(19, 0)
        g.add_edge(19, 39)
        g.add_edge(19, 50)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(3, 5)
        g.add_edge(70, 6)
        g.add_edge(65, 7)
        g.add_edge(55, 8)
        g.add_edge(45, 9)
        result = g.greedy_coloring()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)

    def test_measure_undirected_graph_with_random_data(self):
        """
            Тест измерения времени для неориентированного графа со случайными значениями.
        """
        # given
        all_v = random.randint(1, 501)
        g = Graph(all_v)
        for _ in range(100):
            u, v = random.sample(range(all_v), 2)
            g.add_edge(u, v)

        # when
        start_time = time.perf_counter()
        result = g.greedy_coloring()
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # then
        print("---Program execution time: %s seconds ---" % execution_time)


if __name__ == "__main__":
    unittest.main()
