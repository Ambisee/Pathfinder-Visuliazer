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
def astar_exc(draw, drawpath, node_list, start, end, FPS):
    ''' Execute pathfinding with A* Search Algorithm '''
    pause = False
    count = 0
    start.g_score = 0
    start.h_score = h(start, end)
    start.f_score = start.g_score + start.h_score
    mainqueue = PriorityQueue()
    mainqueue.put((start.f_score, count, start))
    mainqueue_hash = [start]

    while not mainqueue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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
            current.set_end()
            drawpath()
            return

        for neighbor in current.neighbors:
            temp_h = h(neighbor, end)
            temp_g = current.g_score + 1
            temp_f = temp_h + temp_g
            if temp_f < neighbor.f_score:
                neighbor.f_score = temp_f
                neighbor.g_score = temp_g
                neighbor.h_score = temp_h
                neighbor.last_node = current
                if neighbor not in mainqueue_hash:
                    mainqueue.put((neighbor.f_score, count, neighbor))
                    mainqueue_hash.append(neighbor)
                    count += 1
                    neighbor.set_unexplored()
        
        if current != start:
            current.set_explored()
        
        draw()
    
    return

def h(node, end):
    ''' Calculate heuristic value '''
    return abs(end.row - node.row) + abs(end.col - node.col)