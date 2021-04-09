# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:51:22 2021

@author: kevin
"""

import pygame

pygame.init()

size = (400,300)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('移動方塊')


done = False

clock = pygame.time.Clock()


y = 0
x = 0

while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUET:
            done = True
            
    keys =pygame.key.get_pressed()
            
    if keys[pygame.K_LEFT]:
                x-=1
                
    elif keys[pygame.K_RIGHT]:
                x+=1
    elif keys[pygame.K_UP]: 
               y-=1
    elif keys[pygame.K_DOWN]:
               y+=1
    else:
        pass
           
    screen.fill(WHITE)
            
    pygame.draw.rect(screen,RED,[x+10,y+10,10,10])
            
    pygame.display.flip()
            
    clock.tick(60)
pygame.quit()            
            
            
            
            