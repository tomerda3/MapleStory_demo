import pygame
import os
from set_up import *

class Enemy(object):
    global COUNT_UNIVERSE

    def __init__(self, x, y, width, height, end, image_left, image_right,health):
        self.walkRight = image_right
        self.walkLeft = image_left
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(self.walkRight, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.current_health = health
        self.target_health = 500
        self.max_health = 1000
        self.health_bar_length = 400
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change = 5

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight, (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft, (self.x, self.y))
            self.walkCount += 1

    def move(self,player_rect=None):

        # new code starts here
        if player_rect != None:
            if self.x < player_rect.x:
                self.x += self.vel
            else:
                self.x -= self.vel
        # new code end here

        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def basic_health(self):
        BAR_LENGH = 70
        pygame.draw.rect(WIN, RED, (self.x+25, self.y+10, self.target_health/self.health_ratio-30-BAR_LENGH, 15))
        pygame.draw.rect(WIN, WHITE, (self.x+25, self.y+10, self.health_bar_length/2-30-BAR_LENGH ,15), 2)

        red_health_text = ENEMY_HEALTH_FONT.render(
            "HP: " + str(self.current_health), True, WHITE)
        WIN.blit(red_health_text, (self.x+25, self.y-15))

    def get_damage(self, damage):
        print("enemy health before: ", self.current_health)
        if self.target_health - damage <= 0:
            self.target_health = 0
            self.current_health = 0
        else:
            self.target_health -= damage
            self.current_health -= damage

        print("enemy health after: ", self.current_health)


