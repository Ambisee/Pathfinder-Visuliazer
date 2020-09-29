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
from queue import PriorityQueue
import pygame
import sys

# --- Functions --- #
def best_exc(draw, drawpath, node_list, start, end, FPS):
    pause = False
    count = 0
    start.h_score = h(start, end)
    mainqueue = PriorityQueue()
    mainqueue.put((start.h_score, count, start))
    mainqueue_hash = [start]

    while not mainqueue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if pause == False:
                        pause = True
                    else:
                        pause = False
                if event.key == pygame.K_SPACE:
                    return
        
        if pause:
            continue

        current = mainqueue.get()[2]
        mainqueue_hash.remove(current)

        if current == end:
            drawpath()
            return

        for neighbor in current.neighbors:
            temp_h = h(neighbor, end)
            if temp_h < neighbor.h_score:
                neighbor.h_score = temp_h
                neighbor.last_node = current
                if neighbor not in mainqueue_hash:
                    mainqueue.put((neighbor.h_score, count, neighbor))
                    mainqueue_hash.append(neighbor)
                    count += 1
                    neighbor.set_unexplored()
        
        if current != start:
            current.set_explored()
        
        draw()

def h(node, end):
    return abs(end.row - node.row) + abs(end.col - node.col)