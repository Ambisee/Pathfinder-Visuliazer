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

# --- Functions --- #
def first_exec(draw, node_list, start, end, FPS):
    ''' Execute pathfinding with Breadth-First Search Algorithm '''
    pause = False
    queue = [start]

    while len(queue) != 0:
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
        
        current = queue.pop(0)
        for neighbor in current.neighbors:
            if not neighbor.isUnexplored() and not neighbor.isExplored():
                neighbor.set_unexplored()
                neighbor.last_node = current
                queue.append(neighbor)

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
    current = end.last_node
    end.set_end()
    while current != start:
        current.set_path()
        current = current.last_node
        draw()