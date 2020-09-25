'''
Module to contain all relevant
function related to placement of graphical
elements within the window
'''

# --- Modules --- #
import pygame

# --- Variables --- #
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (196, 196, 196)
GREY = (125, 125, 125)

rect_width = 150
font = pygame.font.SysFont("arial", 15)

keycontrol = ["LM - Draw", "RM - Erase", "Space - Execute/Stop", "Escape - Pause/Resume", "C - Clear Grid"]
labels = []
for text in keycontrol:
    x = font.render(text, True, (0, 0, 0))
    labels.append(x)

# --- Classes --- #
class AlgorithmSel:
    def __init__(self, text, alg):
        ''' Create algorithm selector button object '''
        self.color = WHITE
        self.text = text
        self.textcolor = BLACK
        self.label = font.render(text, True, self.textcolor)
        self.alg = alg

    def draw(self, window, x, y):
        pygame.draw.rect(window, self.color, (x, y, rect_width, rect_width/2))
        window.blit(self.label, (x + (rect_width//2 - self.label.get_width()//2), y + (rect_width//4 - self.label.get_height()//2)))
    
    def set_hover(self):
        self.color = LIGHT_GREY

    def set_selected(self):
        self.color = GREY
        self.textcolor = WHITE
    
    def set_unselected(self):
        self.color = WHITE
        self.textcolor = BLACK
    
    def isHover(self):
        return self.color == LIGHT_GREY
    
    def isSelected(self):
        return self.color == GREY

# --- Functions --- #
def redraw_window(window, node_list, color, WIDTH, RC, GAP):
    ''' Clear, draw, and update window '''
    for row in range(RC):
        for col in range(RC):
            node_list[row][col].draw(window)
    
    for row in range(RC + 1):
        pygame.draw.line(window, color, (0, row * GAP), (WIDTH, row * GAP))
    for column in range(RC):
        pygame.draw.line(window, color, (column * GAP, 0), (column * GAP, WIDTH))
    
    pygame.draw.line(window, (0, 0, 0), (WIDTH, 0), (WIDTH, WIDTH + 100))
    draw_keycontrol(window, WIDTH)
    
    pygame.display.update()

def redraw_window2(window, node_list, color, sels, WIDTH, RC, GAP):
    window.fill((255,255,255))
    drawsel(window, sels, WIDTH)
    redraw_window(window, node_list, color, WIDTH, RC, GAP)

def drawpath(window, node_list, start, end, color, sels, WIDTH, RC, GAP, FPS):
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
        redraw_window2(window, node_list, color, sels, WIDTH, RC, GAP)

    end.set_end()
    redraw_window(window, node_list, color, WIDTH, RC, GAP)

def draw_keycontrol(window, WIDTH):
    ''' Draw the keycontrol instruction '''
    height = 0
    x = 0
    for text in labels:
        if WIDTH + height <= WIDTH + 100 - text.get_height():
            window.blit(text, (x, WIDTH + height))
            height += text.get_height()
        else:
            height = 0
            x += 200
            pygame.draw.line(window, (125, 125, 125), (x - 10, WIDTH), (x - 10, WIDTH + 100))
            window.blit(text, (x, WIDTH + height))
            height += text.get_height()

def init_selectors():
    ''' Initialize list of selectors '''
    selectors = []
    selectors.append(AlgorithmSel("Breadth First Search (Q)", "First"))
    selectors.append(AlgorithmSel("Dijkstra's Algorithm (W)", "Dijkstra"))
    selectors.append(AlgorithmSel("A* Search (E)", "A"))
    return selectors

def drawsel(window, sels, WIDTH):
    ''' Draw selectors '''
    x = WIDTH
    y = 0
    for item in sels:
        item.draw(window, x, y)
        y += rect_width/2