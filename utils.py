import csv


def build_graph(edgeFile):
    with open(edgeFile) as file:
        edges = csv.DictReader(file)
        graph = {}
        for edge in edges:
            if graph.get(edge['start']) is None:
                graph[edge['start']] = [edge]
            else:
                graph[edge['start']].append(edge)

        return graph

def average_speed_limit(edgeFile):
    with open(edgeFile) as file:
        edges = csv.DictReader(file)

        speeds = [float(edge['speed limit']) for edge in edges]

        return sum(speeds)/ len(speeds)



def load_heuristics(heuristicfile):
    with open(heuristicfile) as file:
        reader = csv.DictReader(file)
        heuristics = {}
        for line in reader:
            heuristics[line['node']] = {
                '1079387396': line['1079387396'],
                '1737223506': line['1737223506'],
                '8513026827': line['8513026827']
            }
        return heuristics
    



def check_duplicate(l):
    if len(set(l)) < len(l): 
        print('DUP')