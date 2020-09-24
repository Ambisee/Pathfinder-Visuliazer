'''
Module to contain all relevant
function related to placement of graphical
elements within the window
'''

# --- Modules --- #
import pygame

# --- Functions --- #
def redraw_window(window, node_list, color, WIDTH, RC, GAP):
    ''' Clear, draw, and update window '''
    window.fill((255, 255, 255))
    for row in range(RC):
        for col in range(RC):
            node_list[row][col].draw(window)
    
    for row in range(RC + 1):
        pygame.draw.line(window, color, (0, row * GAP), (WIDTH, row * GAP))
    for column in range(RC):
        pygame.draw.line(window, color, (column * GAP, 0), (column * GAP, WIDTH))
    
    pygame.draw.line(window, (0, 0, 0), (WIDTH, 0), (WIDTH, WIDTH + 100))

    pygame.display.update()

def draw_keyboard(window, WIDTH):
    font1 = pygame.font.SysFont("Courier", 15)
    
    keycontrol = ["LM - Draw", "RM - Erase", ""]

def drawpath(window, node_list, start, end, color, WIDTH, RC, GAP, FPS):
    ''' Draw the path '''
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
        redraw_window(window, node_list, color, WIDTH, RC, GAP)

    end.set_end()
    redraw_window(window, node_list, color, WIDTH, RC, GAP)