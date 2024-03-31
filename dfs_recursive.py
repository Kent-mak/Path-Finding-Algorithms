from utils import build_graph
import sys


edgeFile = 'edges.csv'

graph = build_graph(edgeFile)
visited = set()


def dfs(start, end):
    # Begin your code (Part 2)
    '''
    The recursive implementation of DFS intuitively describes the behavior of DFS at each node, which is inspect, then perform DFS for all childeren nodes.
    A point worth noting is that python has recursion limit set at 1000, however for certain cases the recursive method may exceed its max recursion depth.
    therefore "sys.setrecursionlimit(23657)" can be added to the main function.
    '''
    start = str(start)
    end = str(end)

    visited.add(start)
    
    if graph.get(start) is None:
        return [], 0, 0


    for edge in graph[start]:
        if edge['end'] in visited:
            continue

        if edge['end'] == end:
            return [int(edge['start']), int(edge['end'])], float(edge['distance']), len(visited)+1
        
        cur_path, cur_dist, num_visited = dfs(int(edge['end']), end)
        
        if len(cur_path) > 0 :   
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
