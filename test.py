import unittest
from main import Graph


class TestGraph(unittest.TestCase):

    def test_undirected_coloring(self):
        """
        Неориентированный связный граф

        Тест для неориентированного связного графа.
        Проверяет правильность раскраски графа с циклической структурой.
        """
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 0)
        g.add_edge(1, 4)
        result = g.greedy_coloring()
        self.assertEqual(result, [0, 1, 0, 1, 2])

    def test_disconnected_graph(self):
        """
        Неориентированный несвязный граф

        Тест для неориентированого несвязного графа.
        Проверяет правильность раскраски двух независимых компонент графа.
        """
        g = Graph(6)
        g.add_edge(0, 1)
        g.add_edge(2, 3)
        result = g.greedy_coloring()
        self.assertEqual(result[:2], [0, 1])
        self.assertEqual(result[2:4], [0, 1])

    def test_directed_coloring(self):
        """
        Ориентированный связный граф

        Тест для ориентированного связныого графа.
        Проверяет раскраску графа с направленными рёбрами.
        """
        g = Graph(5)
        g.add_edge(0, 1, directed=True)
        g.add_edge(1, 2, directed=True)
        g.add_edge(2, 3, directed=True)
        g.add_edge(3, 4, directed=True)
        g.add_edge(4, 0, directed=True)
        result = g.greedy_coloring_directed()
        self.assertEqual(result, [0, 1, 0, 1, 2])

    def test_directed_disconnected_graph(self) -> None:
        """
        Ориентированный несвязный граф

        Тест для ориентированного несвязного графа.
        Проверяет правильность раскраски графа с несколькими независимыми компонентами.
        """
        g = Graph(6)
        g.add_edge(0, 1, directed=True)
        g.add_edge(2, 3, directed=True)
        result = g.greedy_coloring_directed()
        self.assertEqual(result[:2], [0, 1])
        self.assertEqual(result[2:4], [0, 1])

    def test_cycle_graph(self):
        """
        Циклический граф

        Тест для графа с циклом.
        Проверяет правильность раскраски графа, где вершины образуют замкнутый цикл.
        """
        g = Graph(6)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 0)
        result = g.greedy_coloring()
        self.assertEqual(result, [0, 1, 0, 1, 0, 1])

    def test_acyclic_graph(self):
        """
        Ациклический граф

        Тест для ациклического графа.
        Проверяет правильность раскраски линейного графа без циклов.
        """
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        result = g.greedy_coloring()
        self.assertEqual(result, [0, 1, 0, 1])


if __name__ == "__main__":
    unittest.main()
