'''
Breadth-First Search Algorithm package :

Breadth-First Search Algorithm is a pathfinding algorithm initially invented
by Konrad Zuse in 1945, which was not published until 1972. It was reinvented later on
by Edward F. Moore in 1959. It finds the shortest path to traverse through a graph by 
moving to a node and explore all the neighbor nodes before moving on to the next node.

source: https://en.wikipedia.org/
'''

# --- Modules --- #
import pygame
import queue

# --- Functions --- #
def first_exec(draw, node_list, start, end, FPS):
    ''' Execute pathfinding with Breadth-First Search Algorithm '''
    pause = False
    mainqueue = queue.Queue()
    mainqueue.put(start)

    while not mainqueue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if pause == False:
                        pause = True
                        # pause_menu()
                    else:
                        pause = False
                if event.key == pygame.K_SPACE:
                    return

        if pause:
            continue
        
        current = mainqueue.get()
        for neighbor in current.neighbors:
            if not neighbor.isUnexplored() and not neighbor.isExplored():
                neighbor.set_unexplored()
                neighbor.last_node = current
                mainqueue.put(neighbor)

        if current != start:
            current.set_explored()
        elif current == start:
            current.set_start()
        if current == end:
            first_drawpath(draw, node_list, start, end, FPS)
            return
        draw()

def first_drawpath(draw, node_list, start, end, FPS):
    ''' Draw the path - Breadth-First Search '''
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