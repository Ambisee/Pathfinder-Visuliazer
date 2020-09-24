'''
Main Execution File
of Pathfinder Visualizer
'''

# --- Modules --- #
import pygame
import os
from win32api import GetSystemMetrics
from pf_pack.breadth_first import *
from pf_pack.dijkstra import *
from pf_pack.a_star import *
from pf_pack.node import *
from pf_pack.draw import *

# --- Variables --- #
WIDTH = 500
window_res = (WIDTH + 100, WIDTH + 100)
# os.environ['SDL_VIDEO_WINDOW_POS'] = f'{GetSystemMetrics(0)//2 - WIDTH//2}, {GetSystemMetrics(1)//2 - (WIDTH + 100)//2}'
os.environ['SDL_VIDEO_CENTERED'] = "1"
pygame.init()

# --- Pygame Window --- #
RC = 50
GAP = WIDTH // RC
screen = pygame.display.set_mode(window_res)
pygame.display.set_caption("Pathfinder Visualizer")
    
# --- Text Objects --- #
font1 = pygame.font.SysFont('comicsans', 20)
font2 = pygame.font.SysFont('system', 20)
text = ['L Mouse - Draw', 'R Mouse - Erase', 'Space - Execute/Stop Execution', "C - Clear Grid", 'Escape - Resume/Pause']
label = []

# --- Function --- #
def get_coor(x, y):
    row = x // GAP
    col = y // GAP
    return row, col

def createBorder(node_list):
    ''' Return a list of nodes which are placed on the edge of the grid '''
    wall = []
    for row in range(RC):
        wall.append(node_list[row][0])
        wall.append(node_list[row][RC - 1])
    for col in range(RC):
        wall.append(node_list[0][col])
        wall.append(node_list[RC - 1][col])
    return wall

def main():
    ''' Main execution function '''
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    start_node = None
    end_node = None
    node_list = [[Node(row, col, GAP) for col in range(RC)] for row in range(RC)]
    border = createBorder(node_list)

    drawfunc = lambda: redraw_window(screen, node_list, GREY, WIDTH, RC, GAP)
    drawpathfunc = lambda: drawpath(screen, node_list, start_node, end_node, GREY, WIDTH, RC, GAP, FPS)

    for node in border:
        node.set_wall()
    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start_node != None and end_node != None:
                    for row in node_list:
                        for node in row:
                            node.update_neighbors(node_list, RC)
                    dijkstra_exec(drawfunc, drawpathfunc, node_list, start_node, end_node, FPS)
                
                if event.key == pygame.K_j and start_node != None and end_node != None:
                    for row in node_list:
                        for node in row:
                            node.update_neighbors(node_list, RC)
                    first_exec(drawfunc, drawpathfunc, node_list, start_node, end_node, FPS)
                
                if event.key == pygame.K_k and start_node != None and end_node != None:
                    for row in node_list:
                        for node in row:
                            node.update_neighbors(node_list, RC)
                    astar_exc(drawfunc, drawpathfunc, node_list, start_node, end_node, FPS)

                if event.key == pygame.K_c:
                    start_node = None
                    end_node = None
                    for row in node_list:
                        for node in row:
                            if node not in border:
                                node.reset()
                                node.set_none()
            
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                row_click, col_click = get_coor(x, y)
                try:
                    node = node_list[row_click][col_click]
                except IndexError:
                    pass

                if start_node == None and node.isEmpty():
                    start_node = node
                    node.set_start()
                elif end_node == None and node.isEmpty():
                    end_node = node
                    node.set_end()
                elif node.isEmpty():
                    node.set_wall()
            
            if pygame.mouse.get_pressed()[2]:
                x, y = pygame.mouse.get_pos()
                row_click, col_click = get_coor(x, y)
                try:
                    node = node_list[row_click][col_click]
                except IndexError:
                    pass

                if node.isStart():
                    start_node = None
                    node.set_none()
                elif node.isEnd():
                    end_node = None
                    node.set_none()
                elif node not in border and not node.isEmpty():
                    node.set_none()

        redraw_window(screen, node_list, GREY, WIDTH, RC, GAP)

# --- Main Execution --- #
if __name__ == "__main__":
    main()