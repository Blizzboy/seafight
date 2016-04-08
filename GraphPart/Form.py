import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Huy, World!')

screen = pygame.Surface((800, 600))

bg = pygame.image.load('D:\Python3.2.2\Lib\site-packages\pygame\chmo.gif') # Указываете путь, куда поместили файл с изображением
music = ('D:\Python3.2.2\Lib\site-packages\pygame\catgroove.mp3') # Путь к аудиофайлу
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play()
done = True                         # Цикл, отвечающий собственнно за вывод формы
while done:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			done = False 

	screen.fill(0)
	window.blit(bg, (0, 0))
	pygame.display.flip()