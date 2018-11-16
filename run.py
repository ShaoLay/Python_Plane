import pygame
from pygame.locals import *
from sys import exit


SCREEN_WIDTH = 400
SCREEN_HIGHT = 800

# 初始化游戏,并设置游戏窗口的大小
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption('飞机大战')

# 载入背景图片
background = pygame.image.load('resources/image/background.png')

while True:
    # 绘制背景
    screen.fill(0)
    screen.blit(background, (0,0))

    # 更新屏幕
    pygame.display.update()

    # 处理游戏退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()