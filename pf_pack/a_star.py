'''
A* Search Algorithm Package :

A* Search Algorithm is a pathfinding algorithm is a pathfinding and graph-traversing 
algorithm published by Peter Hart, Nils Nilsson and Bertram Raphael in 1968. It can be
seen as an extension to Dijkstra's Algorithm with the usage of heuristic to help find 
the shortest route.

source: https://en.wikipedia.org/
'''

# --- Modules --- #
import pygame
from queue import PriorityQueue

# --- Functions --- #
def astar_exc(draw, node_list, start, end, FPS):
    ''' Execute pathfinding with A* Search Algorithm '''
    pause = False
    count = 0
    start.shortest_dist = 0
    start.

def h(node, end):
    ''' Calculate heuristic value '''
    return abs(end.row - node.row) + abs(end.col - node.col)