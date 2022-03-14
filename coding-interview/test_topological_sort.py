from collections import defaultdict, deque
from typing import Dict, List


def topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    in_degree: Dict[int, int] = defaultdict(int)
    n = len(graph.keys())
    for _, vs in graph.items():
        for v in vs:
            in_degree[v] += 1
    res: List[int] = []
    q = deque([i for i in range(n) if in_degree[i] == 0])
    while q:
        cur = q.popleft()
        res.append(cur)
        for v in graph[cur]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    return res


def test_topological_sort() -> None:
    dependency_graph1: Dict[int, List] = {
        0: [5],
        1: [3, 6],
        2: [5, 7],
        3: [0, 7],
        4: [1, 2, 6],
        5: [],
        6: [7],
        7: [0],
    }
    expected1 = [4, 1, 2, 3, 6, 7, 0, 5]
    achieved1 = topological_sort(dependency_graph1)
    assert expected1 == achieved1
    dependency_graph2: Dict[int, List] = {
        0: [],
        1: [],
        2: [3],
        3: [1],
        4: [0, 1],
        5: [0, 2],
    }
    expected2 = [4, 5, 0, 2, 3, 1]
    achieved2 = topological_sort(dependency_graph2)
    assert expected2 == achieved2
