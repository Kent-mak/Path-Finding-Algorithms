from utils import build_graph, check_duplicate
import sys


edgeFile = 'edges.csv'

graph = build_graph(edgeFile)
visited = set()


def dfs(start, end):
    # Begin your code (Part 2)
    start = str(start)
    end = str(end)

    visited.add(start)
    
    # print(f'{start}: ')
    if graph.get(start) is None:
        # print(start)
        return [], 0, 0


    for edge in graph[start]:
        # print(f'{start}: {edge['end']}')
        if edge['end'] in visited:
            continue

        if edge['end'] == end:
            # print(edge['end'])
            return [int(edge['start']), int(edge['end'])], float(edge['distance']), len(visited)+1
        
        cur_path, cur_dist, num_visited = dfs(int(edge['end']), end)
        
        if len(cur_path) > 0 :   
            # print(edge['start'])
            return [int(edge['start'])]+cur_path, cur_dist + float(edge['distance']), num_visited
        
    
    return [], 0, len(visited)

    

    
    raise NotImplementedError("To be implemented")
    # End your code (Part 2)


if __name__ == '__main__':
    sys.setrecursionlimit(23657)
    path, dist, num_visited = dfs(2270143902, 1079387396)
    # print(path)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
