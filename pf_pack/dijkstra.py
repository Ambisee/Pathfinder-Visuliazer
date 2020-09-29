'''
Dijkstra's Algorithm package :

Djikstra's Algorithm is a pathfinding algorithm conceived by computer scientiest
Edgar Wybe Dijkstra in 1956 and published three years later. It finds the shortest path
through a graph by picking an unvisited node and calculate the shortest distance towards
other unvisited nodes.

souce: https://en.wikipedia.org/
'''

# --- Modules --- #
from queue import PriorityQueue
import pygame

# --- Functions --- #
def dijkstra_exec(draw, drawpath, node_list, start, end, FPS):
    ''' Executes pathfinding with Dijkstra's Algorithm '''
    pause = False
    count = 0
    start.g_score = 0
    start.last_node = start
    mainqueue = PriorityQueue()
    mainqueue.put((0, count, start))
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
            temp_short = current.g_score + 1
            if temp_short < neighbor.g_score:
                neighbor.g_score = temp_short
                neighbor.last_node = current
                if neighbor not in mainqueue_hash:
                    count += 1
                    mainqueue_hash.append(neighbor)
                    mainqueue.put((neighbor.g_score, count, neighbor))
                    neighbor.set_unexplored()

        if current != start:
            current.set_explored()
        draw()