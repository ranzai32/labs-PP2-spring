import pygame
from tkinter import *
from PIL import Image, ImageDraw
import PIL


def main():
    pygame.init()
    WIDTH = 500
    HEIGHT = 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    WHITE = (255,255,255)
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    # class PaintGUI:

    #     def __init__(self):
    #         self.root = Tk()
    #         self.root.title("Paint")

    #         self.brush_w = 15
    #         self.current_color = "#000000"

    #         self.cnv = Canvas(self.root, width=WIDTH-10, height=HEIGHT-10, bg="white")
    #         self.cnv.pack()
    #         self.cnv.bind("<B1-Motion>", self.paint)

    #         self.btn_frame = Frame(self.root)
    #         self.btn_frame.pack(fill=X)

    #         self.btn_frame.columnconfigure(0, weight=1)
    #         self.btn_frame.columnconfigure(1, weight=1)
    #         self.btn_frame.columnconfigure(2, weight=1)

    #         self.clear_btn = Button(self.btn_frame, text="Очистить", command=self.clear)
    #         self.clear_btn.grid(row=1, column=0, sticky="W+E")

    #         self.rec_btn = Button(self.btn_frame, text="Прямоугольник", command=self.rec)
    #         self.rec_btn.grid(row=1, column=1, sticky="W+E")

    #         self.bminus_btn = Button(self.btn_frame, text="Тоньше", command=self.brush_minus)
    #         self.bminus_btn.grid(row=0, column=0, sticky="W+E")

    #         self.bplus_btn = Button(self.btn_frame, text="Толще", command=self.brush_plus)
    #         self.bplus_btn.grid(row=0, column=1, sticky="W+E")

    #         self.color_btn = Button(self.btn_frame, text="Изменить цвет", command=self.change_color)
    #         self.color_btn.grid(row=1, column=2, sticky="W+E")

    #     def paint(self, event):
    #     # Метод для рисования
    #         pass

    #     def change_color(self):
    #     # Метод для изменения цвета
    #         pass

    #     def brush_plus(self):
    #     # Метод для увеличения размера кисти
    #         pass

    #     def brush_minus(self):
    #     # Метод для уменьшения размера кисти
    #         pass

    #     def rec(self):
    #     # Метод для рисования прямоугольника
    #         pass

    #     def clear(self):
    #     # Метод для очистки холста
    #         pass


    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[:]
                
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()