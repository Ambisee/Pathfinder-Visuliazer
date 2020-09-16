'''
Breadth-First Search Algorithm package :

Breadth-First Search Algorithm is a pathfinding algorithm initially invented
by Konrad Zuse in 1945, which was not published until 1972. It was reinvented later on
by Edward F. Moore in 1959. It finds the shortest path to traverse through a graph by 
moving to a node and explore all the neighbor nodes before moving on to the next node.

source: https://en.wikipedia.org/
'''

# --- Modules --- #
import queue
import pygame

# --- Functions --- #
def first_exec(draw, node_list, start, end, FPS):
    ''' Execute pathfinding with Breadth-First Search Algorithm '''
    pause = False
    path = []
    mainqueue = queue.Queue()
    n_l = [start]
    mainqueue.put(n_l)

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
        
        path = mainqueue.get()
        for neighbor in path[-1].neighbors:
            if not neighbor.isExplored():
                x = path.copy()
                x.append(neighbor)
                mainqueue.put(x)

        if not path[-1].isStart() or not path[-1].isEnd():
            path[-1].set_explored()
        if path[-1] == end:
            first_drawpath(draw, start, end, path, FPS)
            return
        draw()
    
    if not isEnd(end, path):
        return
    else:
        first_drawpath(draw, start, end, path, FPS)
        return
    
def firs_exec2(draw, node_list, start, end, FPS):
    row = start.row
    col = start.col
    mainqueue = queue.Queue()
    mainqueue.put("")
    path = ""

    while not isEnd(node_list, end):
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

        path = mainqueue.get()
        node = path_end(node_list, start, path)

        if isEnd(node, end):
            first_drawpath(draw, node_list, start,end, path, FPS)
            return

        for dir in ["L", "R", "U", "D"]:
            temp = path + dir
            temp_node = path_end(node_list, start, temp)
            if valid(temp_node):
                mainqueue.put(temp)
        
        node.set_explored()
        draw()

def path_end(node_list, start, path):
    row = start.row
    col = start.col

    for dir in path:
        if dir == "L":
            col -= 1
        elif dir == "R":
            col += 1
        elif dir == "U":
            row -= 1
        elif dir == "D":
            row += 1
    
    return node_list[row][col]

def valid(node):
    return not node.isWall()
    
def isEnd(node, end):
    return node == end
    
def first_drawpath(draw, node_list, start, end, path, FPS):
    ''' Draw the path - Breadth-First Search '''
    row = start.row
    col = start.col
    start.set_start()
    end.set_end()

    for dir in path:
        if dir == "L":
            col -= 1
        elif dir == "R":
            col += 1
        elif dir == "U":
            row -= 1
        elif dir == "D":
            row += 1
        
        node_list[row][col].set_path()
        draw()