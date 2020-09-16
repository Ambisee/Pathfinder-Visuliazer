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

# --- Function --- #
def dijkstra_exec(draw, node_list, start, end, FPS):
    ''' Executes pathfinding with Dijkstra's Algorithm '''
    pause = False
    count = 0
    start.shortest_dist = 0
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
                        pause_menu()
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
            dijkstra_drawpath(draw, node_list, end, start, FPS)
            return
        
        for neighbor in current.neighbors:
            temp_short = current.shortest_dist + 1
            if temp_short < neighbor.shortest_dist:
                neighbor.shortest_dist = temp_short
                neighbor.last_node = current
                if neighbor not in mainqueue_hash:
                    count += 1
                    mainqueue_hash.append(neighbor)
                    mainqueue.put((neighbor.shortest_dist, count, neighbor))
                    neighbor.set_unexplored()

        if current != start:
            current.set_explored()
        draw()

def dijkstra_drawpath(draw, node_list, end, start, FPS):
    ''' Draw the path - Dijkstra's '''
    current = end
    timer = 0
    n_list = []
    while current != start:
        n_list.append(current.last_node)
        current = current.last_node

    n_list.reverse()
    for node in n_list:
        start.set_start()
        node.set_path()
        while timer <= FPS * 1000:
            timer += 1
        timer = 0
        draw()

    end.set_end()
    draw()