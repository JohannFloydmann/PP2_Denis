import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
my_ft_font = pygame.freetype.SysFont('Verdana', 50)

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colors = [colorRED, colorBLUE, colorWHITE]

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

mouse_x, mouse_y = pygame.mouse.get_pos()

curr_x = mouse_x
curr_y = mouse_y

prev_x = mouse_x
prev_y = mouse_y

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_figure(figure_index, color_index):
    if figure_index == 0:   # Line
        pygame.draw.line(screen, colors[color_index], (prev_x, prev_y), (curr_x, curr_y), THICKNESS)
    elif figure_index == 1: # Rectangle
        pygame.draw.rect(screen, colors[color_index], calculate_rect(prev_x, prev_y, curr_x, curr_y), THICKNESS)
    elif figure_index == 2: # Circle
        pygame.draw.circle(screen, colors[color_index], (prev_x, prev_y), math.sqrt( pow(curr_x-prev_x, 2) + pow(curr_y-prev_y, 2) ), THICKNESS)
    elif figure_index == 3: # Eraser
        pygame.draw.rect(screen, colorBLACK, calculate_rect(prev_x, prev_y, curr_x, curr_y))
    elif figure_index == 4: # Right Triangle
        pygame.draw.polygon(screen, colors[color_index], [(prev_x, prev_y), (curr_x, curr_y), (curr_x + abs(curr_y-prev_y)/2, curr_y + abs(curr_x-prev_x)/2)], THICKNESS)
    elif figure_index == 5: # Equilateral Triangle
        pygame.draw.polygon(screen, colors[color_index], [(prev_x, prev_y), (curr_x + abs(curr_y-prev_y)/2, curr_y + abs(curr_x-prev_x)/2), (curr_x - abs(curr_y-prev_y)/2, curr_y - abs(curr_x-prev_x)/2)], THICKNESS)

figures = ['Line', 'Rectangle', 'Circle', 'Eraser', 'Right Triangle', 'Equilateral Triangle']

figure_index = 0
color_index = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # print("LMB pressed!")
            LMBpressed = True
            curr_x = event.pos[0]
            curr_y = event.pos[1]
            prev_x = event.pos[0]
            prev_y = event.pos[1]
        if event.type == pygame.MOUSEMOTION:
            # print("Position of the mouse:", event.pos)
            curr_x = event.pos[0]
            curr_y = event.pos[1]
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # print("LMB released!")
            LMBpressed = False
            draw_figure(figure_index, color_index)
            base_layer.blit(screen, (0, 0))
        
        if event.type == pygame.KEYDOWN: 
            # thickness change
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1
            
            # figure change
            if event.key == pygame.K_UP:
                figure_index += 1
                if figure_index >= len(figures):
                    figure_index = 0
            if event.key == pygame.K_DOWN:
                figure_index -= 1
                if figure_index < 0:
                    figure_index = len(figures) - 1

            # color change
            if event.key == pygame.K_RIGHT:
                color_index += 1
                if color_index >= len(colors):
                    color_index = 0
            if event.key == pygame.K_LEFT:
                color_index -= 1
                if color_index < 0:
                    color_index = len(colors) - 1

    screen.blit(base_layer, (0, 0))

    if LMBpressed:
        draw_figure(figure_index, color_index)


    pygame.draw.rect(screen, colorBLACK, (0, 0, WIDTH, 60))
    my_ft_font.render_to(screen, (10, 10), figures[figure_index], colors[color_index] if color_index != 3 else colorWHITE)

    pygame.display.flip()
    clock.tick(60)