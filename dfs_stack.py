from collections import deque
from utils import build_graph
edgeFile = 'edges.csv'

graph = build_graph(edgeFile)


def dfs(start, end):
    # Begin your code (Part 2)
    visited = set()
    
    visited.add(str(start))
    stack = deque()
    for edge in graph[str(start)]:
        stack.append([edge])
        
    path = None

    while len(stack) > 0:
        cur_path = stack.pop()
        if cur_path[-1]['end'] in visited:
            continue
        visited.add(cur_path[-1]['end'])

        if cur_path[-1]['end'] == str(end):
            path = cur_path
            break

        if graph.get(cur_path[-1]['end']) is not None:
            for edge in graph.get(cur_path[-1]['end']):
                new_path = cur_path.copy()
                new_path.append(edge)
                stack.append(new_path)
    
    if path is None:
        return [], 0, len(visited)
    dfs_path = [int(edge['start']) for edge in path]
    dfs_path.append(int(path[-1]['end']))

    nodes = set()
    for node in dfs_path:
        if node in nodes:
            print ('duplicate exist')
        nodes.add(node)



    # print(dfs_path)
    distance = 0
    for edge in path:
        distance += float(edge['distance'])

    return dfs_path, distance, len(visited)
    
        
    

    raise NotImplementedError("To be implemented")
    # End your code (Part 2)


if __name__ == '__main__':
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
