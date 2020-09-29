'''
Greedy Best-First Search Algorithm

Greedy Best-First Search Algorithm is a pathfinding and graph traversing algorithm 
that utilizes a heuristic value to find the shortest path to the goal. The heuristic
value predicts how close the path is to the end goal. This algorithm later was combined
with the Dijkstra's Algorithm, which uses the calculation of shortest distance from the
start, into the A* Search Algorithm.

source : https://en.wikipedia.org/
'''
# --- Modules --- #
import pygame

# --- Functions --- #
def best_exc(draw, drawpath, node_list, start, end, FPS);