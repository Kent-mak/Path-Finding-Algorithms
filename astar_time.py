from queue import PriorityQueue
import utils
from dataclasses import dataclass, field

@dataclass
class Node:
    time_from_start: float = 0
    path: list[str] = field(default_factory=list)

edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'

graph = utils.build_graph(edgeFile)
dist_heuristic = utils.load_heuristics(heuristicFile)
avg_speed = utils.average_speed_limit(edgeFile)

def avg_edge_speed_limit(node):
    if graph.get(node) is None:
        return 0
    limits = [float(edge['speed limit']) for edge in graph[node]]
    return sum(limits)/len(limits)


def compute_time_heuristic(node, end):
    speed = avg_edge_speed_limit(node)
    if speed == 0:
        return float('inf')
    return float(dist_heuristic[node][end])/speed


def astar_time(start, end):
    # Begin your code (Part 6)
    start = str(start)
    end = str(end)

    open = PriorityQueue()
    closed = set()

    for edge in graph[start]:
        heuristic = compute_time_heuristic(edge['end'], end)
        g = float(edge['distance'])/ float(edge['speed limit'])
        f = g + heuristic
        open.put((f,open.qsize(), Node(g, [start, edge['end']])))

    while open.qsize() > 0:
        top = open.get()
        cur_node = top[2]
        # print(cur_node.path[-1])
        closed.add(cur_node.path[-1])
        if graph.get(cur_node.path[-1]) is None:
            continue
        
        for edge in graph[cur_node.path[-1]]:
            if edge['end'] in closed: 
                continue

            time = float(edge['distance'])/ float(edge['speed limit'])
            time += cur_node.time_from_start 
            
            if edge['end'] == end:
                found_path = [int(i) for i in cur_node.path]
                found_path.append(int(edge['end']))
                return found_path, time, len(closed) + 1
            
            f = time + compute_time_heuristic(edge['end'], end)

            new_path = cur_node.path.copy()
            new_path.append(edge['end'])
            open.put((f,open.qsize(), Node(time, new_path)))
    
    return [], 0, len(closed)

    raise NotImplementedError("To be implemented")
    # End your code (Part 6)


if __name__ == '__main__':
    path, time, num_visited = astar_time(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total second of path: {time}')
    print(f'The number of visited nodes: {num_visited}')
