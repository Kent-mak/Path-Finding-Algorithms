from collections import deque
from utils import build_graph
edgeFile = 'edges.csv'



def bfs(start, end):
    # Begin your code (Part 1)

    graph = build_graph(edgeFile)

    visited = set()
    visited.add(str(start))
    q = deque()

    for edge in graph[str(start)]:
        q.append([edge])
    
    true_path = None
 
    while len(q) > 0 :
        # print(q)
        
        path = q.popleft()
        if path[-1]['end'] in visited:
            continue
        visited.add(path[-1]['end'])

        if path[-1]['end'] == str(end):
            true_path = path
            break
        
        if graph.get(path[-1]['end']) is None:
            continue
        for edge in graph[path[-1]['end']]:

            new_path = path.copy()
            new_path.append(edge)
            # print(f'{path}')
            q.append(new_path)
        # print('---------')

    node_count = len(visited)

    if true_path is None:
        return [], 0, node_count
    
    bfs_path = [int(edge['start']) for edge in true_path]
    bfs_path.append(int(true_path[-1]['end']))

    total_dist = 0
    for edge in true_path:
        total_dist += float(edge['distance'])
    
    return bfs_path, total_dist, node_count



    # raise NotImplementedError("To be implemented")
    # End your code (Part 1)


if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    # print(path)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
