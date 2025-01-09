import matplotlib.pyplot as plt
import networkx as nx
from typing import List


class Graph:
    def __init__(self, vertices: int) -> None:
        """
        Инициализация графа.

        Args:
            vertices (int): Количество вершин в графе.
        """
        # Количество вершин
        self.vertices = vertices
        # Список смежности
        self.smezh_list = {v: [] for v in range(vertices)}
        # Тип графа
        self.directed = False

    def add_edge(self, u: int, v: int, directed: bool = False) -> None:
        """
        Добавление ребра в граф.

        Args:
            u (int): Первая вершина.
            v (int): Вторая вершина.
            directed (bool, optional): Если True, добавляется ориентированное ребро. По умолчанию False.
        """
        self.smezh_list[u].append(v)
        if not directed:
            self.smezh_list[v].append(u)
        else:
            self.directed = True

    def greedy_coloring(self) -> List[int]:
        """
        Раскраска графа жадным алгоритмом.

        Returns:
            list: Список цветов для каждой вершины.

        Example:
            >>> g = Graph(5)
            >>> g.add_edge(0, 1)
            >>> g.add_edge(1, 2)
            >>> g.add_edge(2, 3)
            >>> g.add_edge(3, 4)
            >>> g.add_edge(4, 0)
            >>> g.greedy_coloring()
            [0, 1, 0, 1, 2]
        """
        result = [-1] * self.vertices  # Цвета вершин, -1 означает нераскрашенную вершину
        result[0] = 0  # Первая вершина раскрашена в цвет 0

        # Массив для отслеживания доступности цветов
        available_colors = [False] * self.vertices

        for u in range(1, self.vertices):
            # Цвета соседей помечены как занятые
            for neighbor in self.smezh_list[u]:
                if result[neighbor] != -1:
                    available_colors[result[neighbor]] = True

            # Нахождение первого доступного цвета
            for color in range(self.vertices):
                if not available_colors[color]:
                    result[u] = color
                    break

            # Сброс доступности цветов
            for neighbor in self.smezh_list[u]:
                if result[neighbor] != -1:
                    available_colors[result[neighbor]] = False

        return result

    def greedy_coloring_directed(self) -> List[int]:
        """
        Раскраска ориентированного графа жадным алгоритмом.

        Returns:
            list: Список цветов для каждой вершины.

        Example:
            >>> g = Graph(5)
            >>> g.add_edge(0, 1, directed=True)
            >>> g.add_edge(1, 2, directed=True)
            >>> g.add_edge(2, 3, directed=True)
            >>> g.add_edge(3, 4, directed=True)
            >>> g.greedy_coloring_directed()
            [0, 1, 2, 3, 4]
        """
        if not self.directed:
            return self.greedy_coloring()

        result = [-1] * self.vertices  # Цвета вершин, -1 означает нераскрашенную вершину
        result[0] = 0  # Первая вершина раскрашена в цвет 0

        # Массив для отслеживания доступности цветов
        available = [False] * self.vertices

        for u in range(1, self.vertices):
            # Цвета соседей (входящих и исходящих рёбер) помечены как занятые
            for neighbor in self.smezh_list[u]:
                if result[neighbor] != -1:
                    available[result[neighbor]] = True
            for vertex, neighbors in self.smezh_list.items():
                if u in neighbors and result[vertex] != -1:
                    available[result[vertex]] = True

            # Нахождение первого доступного цвета
            for color in range(self.vertices):
                if not available[color]:
                    result[u] = color
                    break

            # Сброс доступности цветов
            for neighbor in self.smezh_list[u]:
                if result[neighbor] != -1:
                    available[result[neighbor]] = False
            for vertex, neighbors in self.smezh_list.items():
                if u in neighbors and result[vertex] != -1:
                    available[result[vertex]] = False
        return result

    def visualize(self, coloring: List[int], name_graph: str) -> None:
        """
        Визуализация графа с использованием раскраски.

        Args:
            coloring (list): Список цветов вершин.

        Example:
            >>> g = Graph(5)
            >>> g.add_edge(0, 1)
            >>> g.add_edge(1, 2)
            >>> g.add_edge(2, 3)
            >>> g.add_edge(3, 4)
            >>> g.add_edge(4, 0)
            >>> coloring = g.greedy_coloring()
            >>> g.visualize(coloring)
        """
        G = nx.DiGraph() if self.directed else nx.Graph()

        # Добавляем вершины
        for vertex in self.smezh_list:
            G.add_node(vertex)

        # Добавляем ребра
        for u in self.smezh_list:
            for v in self.smezh_list[u]:
                if not G.has_edge(u, v):
                    G.add_edge(u, v)

        # Определяем цвета вершин
        color_map = [coloring[node] for node in G.nodes]

        # Рисуем граф
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=color_map, cmap=plt.cm.rainbow, node_size=500, font_color="white")
        plt.gcf().canvas.manager.set_window_title(name_graph)
        plt.show()


def create_graph_from_user_input() -> Graph:
    """
    Создаёт граф на основе ввода пользователя с обработкой ошибок.

    Returns:
        Graph: Граф, созданный на основе данных пользователя.
    """
    while True:
        try:
            vertices = int(input("Введите количество вершин в графе: "))
            if vertices <= 0:
                raise ValueError("Количество вершин должно быть больше 0.")
            break
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте ещё раз.")

    g = Graph(vertices)

    while True:
        directed_input = input("Граф ориентированный? (да/нет): ").strip().lower()
        if directed_input in ["да", "yes", "y"]:
            directed = True
            break
        elif directed_input in ["нет", "no", "n"]:
            directed = False
            break
        else:
            print("Ошибка: введите 'да' или 'нет'.")

    print("Введите рёбра в формате 'u v', где u и v — индексы вершин (нумерация с 0).")
    print("Для завершения ввода нажмите Enter.")

    while True:
        edge_input = input("Введите ребро (или Enter для завершения): ").strip()
        if not edge_input:
            break
        try:
            u, v = map(int, edge_input.split())
            if u < 0 or u >= vertices or v < 0 or v >= vertices:
                raise ValueError("Индексы вершин должны быть в пределах [0, количество вершин - 1].")
            g.add_edge(u, v, directed=directed)
        except ValueError as e:
            print(f"Ошибка: {e}. Убедитесь, что вы ввели два корректных индекса, разделённых пробелом.")

    return g


# Пример использования
if __name__ == "__main__":
    try:
        user_graph = create_graph_from_user_input()
        print("Список смежности графа:", user_graph.smezh_list)

        # Выполняем жадную раскраску
        if user_graph.directed:
            coloring = user_graph.greedy_coloring_directed()
        else:
            coloring = user_graph.greedy_coloring()

        print("Результат жадной раскраски:", coloring)

        # Визуализируем граф
        name_graph = "Пользовательский граф"
        user_graph.visualize(coloring, name_graph)
    except Exception as e:
        print(f"Произошла ошибка: {e}. Программа завершена.")
