from queue import PriorityQueue
import utils
edgeFile = 'edges.csv'
graph = utils.build_graph(edgeFile)

def ucs(start, end):
    # Begin your code (Part 3)
    visited = set()
    Q = PriorityQueue()
    Q.put((0, [start]))

    while not Q.empty():
        top = Q.get()
        if top[1][-1] in visited:
            continue
        visited.add(top[1][-1])

        if top[1][-1] == end:
            return top[1], top[0], len(visited)

        if graph.get(str(top[1][-1])) is None: continue

        for edge in graph[str(top[1][-1])]:
            new_path = top[1].copy()
            new_path.append(int(edge['end']))
            Q.put((top[0] + float(edge['distance']), new_path))

    return [], 0, len(visited)




    raise NotImplementedError("To be implemented")
    # End your code (Part 3)


if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
