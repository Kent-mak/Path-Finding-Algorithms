import utils
from queue import PriorityQueue
from dataclasses import dataclass, field
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'

graph = utils.build_graph(edgeFile)
heuristics = utils.load_heuristics(heuristicFile)

@dataclass
class Node:
    dist_to_start: float = 0
    path: list[str] = field(default_factory=list)


def astar(start, end):
    # Begin your code (Part 4)
    start = str(start)
    end = str(end)
    open = PriorityQueue()
    closed = set()

    for edge in graph.get(start):
        f = float(edge['distance']) + float(heuristics[edge['end']][end])
        
        open.put((f, Node(float(edge['distance']), [start, edge['end']])))

    while open.qsize() > 0:
        top = open.get()
        cur_node = top[1]
        closed.add(cur_node.path[-1])
        if graph.get(cur_node.path[-1]) is None:
            continue

        for edge in graph[cur_node.path[-1]]:
            if edge['end'] in closed:
                continue
            
            if edge['end'] == end:
                found_path = [int(i) for i in cur_node.path]
                found_path.append(int(edge['end']))
                return found_path, cur_node.dist_to_start + float(edge['distance']), len(closed)+1

            g = cur_node.dist_to_start + float(edge['distance'])
            f = g + float(heuristics[edge['end']][end])
            new_path = cur_node.path.copy()
            new_path.append(edge['end'])
            open.put((f, Node(g, new_path)))
        

    return [], 0, len(closed)

    raise NotImplementedError("To be implemented")
    # End your code (Part 4)


if __name__ == '__main__':
    path, dist, num_visited = astar(426882161, 1737223506)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
