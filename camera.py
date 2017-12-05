import device
import time
import sys, pygame

pygame.init()

size = width, height = 620, 485
speed = [2, 2]
black = 0, 0, 0

pygame.display.set_caption('Caption')
screen = pygame.display.set_mode(size)

SLEEP_TIME_LONG = 0.1

cam = device(devnum=0, showVideoWindow=0)

while True:
    cam.saveSnapshot('test.jpg', timestamp=3, boldfont=1, quality=75)

    image = pygame.image.load('test.jpg')
    screen.blit(image, speed)
    pygame.display.flip()
    time.sleep(SLEEP_TIME_LONG)

