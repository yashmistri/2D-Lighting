# Yash Mistri
import math
import sys

import pygame

import geometry

pygame.init()

size = width, height = 500, 300
black = [0, 0, 0]
screen = pygame.display.set_mode(size)

rects = [pygame.Rect(0, 0, width, height)]

for j in range(0, 300, 40):
    for i in range(0, 500, 40):
        rects.append(pygame.Rect(i, j, 40, 40))
i = 1.67
a = 0.0
b = 3.14


def test_intersection(screen, o1, e1, o2, e2):
    pygame.draw.line(screen, pygame.Color('white'), o1, e1)
    pygame.draw.line(screen, pygame.Color('white'), o2, e2)

    inter = geometry.get_intersection(o1, e1, o2, e2)
    # print(str(inter))
    if inter != False:
        pygame.draw.circle(screen, pygame.Color('green'), (int(inter[0]), int(inter[1])), 5)
        return inter


def draw_objects(screen, d, e, f):
    line1 = [[0, 50 * math.sin(d) + height / 2], [width, 50 * math.sin(d) + height / 2]]
    line2 = [[(height / 2) * math.cos(e) + width / 2, (height / 2) * math.sin(e) + height / 2],
             [(height / 2) * math.cos(f) + width / 2, (height / 2) * math.sin(f) + height / 2]]
    test_intersection(screen, line1[0], line1[1], line2[0], line2[1])


def draw_rects(screen, rects):
    for rect in rects:
        pygame.draw.rect(screen, pygame.Color('white'), rect, 1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(black)

    line1 = [[width / 2, height / 2], pygame.mouse.get_pos()]
    for i in range(len(rects)):
        for x in geometry.intersects_line_rect(line1, rects[i]):
            pygame.draw.circle(screen, pygame.Color('green'), [int(x[0]), int(x[1])], 5)

    draw_rects(screen, rects)
    pygame.draw.line(screen, pygame.Color('yellow'), line1[0], line1[1])

    pygame.display.flip()
