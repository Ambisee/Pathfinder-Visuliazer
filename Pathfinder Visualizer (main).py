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
window_res = (WIDTH + 150, WIDTH + 100)
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
    algorithm = "BrFS"
    FPS = 60
    start_node = None
    end_node = None
    node_list = [[Node(row, col, GAP) for col in range(RC)] for row in range(RC)]
    border = createBorder(node_list)
    sels = init_selectors()
    sels[0].set_selected()

    drawfunc = lambda: redraw_window2(screen, node_list, GREY, sels, WIDTH, RC, GAP)
    drawpathfunc = lambda: drawpath(screen, node_list, start_node, end_node, GREY, sels, WIDTH, RC, GAP, FPS)

    for node in border:
        node.set_wall()
    
    while run:
        clock.tick(FPS)

        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sels[0].set_selected()
                    algorithm = sels[0].alg
                    for i in range(len(sels)):
                        if i != 0:
                            sels[i].set_unselected()
                if event.key == pygame.K_w:
                    sels[1].set_selected()
                    algorithm = sels[1].alg
                    for i in range(len(sels)):
                        if i != 1:
                            sels[i].set_unselected()
                if event.key == pygame.K_e:
                    sels[2].set_selected()
                    algorithm = sels[2].alg
                    for i in range(len(sels)):
                        if i != 2:
                            sels[i].set_unselected()

                if event.key == pygame.K_SPACE and start_node != None and end_node != None and algorithm != None:
                  for row in node_list:
                      for node in row:
                          node.update_neighbors(node_list, RC)
                  if algorithm == "Dij":
                      dijkstra_exec(drawfunc, drawpathfunc, node_list, start_node, end_node, FPS)
                      screen.fill((255,255,255))
                  elif algorithm == "BrFS":
                      first_exec(drawfunc, drawpathfunc, node_list, start_node, end_node, FPS)
                      screen.fill((255,255,255))
                  elif algorithm == "AS":
                      astar_exc(drawfunc, drawpathfunc, node_list, start_node, end_node, FPS)
                      screen.fill((255,255,255))
                  else:
                      pass

                if event.key == pygame.K_c:
                    start_node = None
                    end_node = None
                    for row in node_list:
                        for node in row:
                            if node not in border:
                                node.reset()
                                node.set_none()
            
            x, y = pygame.mouse.get_pos()
            if x > WIDTH:
                pos = y//(rect_width//2)
                try:
                    if not sels[pos].isHover() and not sels[pos].isSelected():
                        for item in sels:
                            if not item.isSelected():
                                item.set_unselected()                        
                        if not sels[pos].isSelected():
                            sels[pos].set_hover()
                    elif sels[pos].isSelected():
                        for item in sels:
                            if not item.isSelected():
                                item.set_unselected()  
                except:
                    pass
            else:
                for item in sels:
                    if not item.isSelected():
                        item.set_unselected()  

            if pygame.mouse.get_pressed()[0]:
                row_click, col_click = get_coor(x, y)
                try:
                    node = node_list[row_click][col_click]

                    if start_node == None and node.isEmpty():
                        start_node = node
                        node.set_start()
                    elif end_node == None and node.isEmpty():
                        end_node = node
                        node.set_end()
                    elif node.isEmpty():
                        node.set_wall()
                except IndexError:
                    if x > WIDTH:
                        try:
                            pos = y//(rect_width//2)
                            sels[pos].set_selected()
                            algorithm = sels[pos].alg
                            for i in range(len(sels)):
                                if i != pos:
                                    sels[i].set_unselected()
                        except IndexError:
                            pass
            
            if pygame.mouse.get_pressed()[2]:
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

        drawsel(screen, sels, WIDTH)
        redraw_window(screen, node_list, GREY, WIDTH, RC, GAP)

# --- Main Execution --- #
if __name__ == "__main__":
    main()