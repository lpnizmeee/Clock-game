import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption('Tai Xiu')
running = True
GREEN = (152,251,152)
RED = (255,160,122)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (135,206,250)

clock = pygame.time.Clock()
background = WHITE

font = pygame.font.SysFont('sans', 30)
text = font.render("Click this button to change color", True, BLUE)

text_box = text.get_rect()

timer = 0
die1 = 0 
die2 = 0
die3 = 0

random_pos = (50,50)
clock_pos = (400, 520)
circle_color = (255,127,80)
circle_color_invert = (255 - circle_color[0], 255 - circle_color[1], 255 - circle_color[2])

def circle(pos_x, pos_y, num1):
	pygame.draw.circle(screen, circle_color, (pos_x,pos_y), 50)
	number_box = font.render(str(num1), True, circle_color_invert)
	number_rect = number_box.get_rect()
	screen.blit(number_box, (pos_x - number_rect[2] / 2, pos_y - number_rect[3] / 2))

def rect():
	pygame.draw.rect(screen, circle_color, (clock_pos[0],clock_pos[1],rect_box[2],rect_box[3]))
	screen.blit(text2, clock_pos)

while running:		
	screen.fill(background)
	dt = clock.tick(120)
	timer -= dt / 1000
	minute = int(timer // 60)
	second = int(timer % 60)

	text2 = font.render(str(minute) + ":" + str(second), True, BLACK)
	rect_box = text2.get_rect()
	rect()

	if timer < 0:
		timer = 10
		die1 = randint(1,6)
		die2 = randint(1,6)
		die3 = randint(1,6)


	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen, RED, (random_pos[0],random_pos[1],text_box[2],text_box[3]))
	screen.blit(text, random_pos)

	circle(100,200,die1)
	circle(400,200,die2)
	circle(250,400,die3)

	if (random_pos[0]<mouse_x) and (mouse_x<(random_pos[0]+text_box[2])) and (random_pos[1]<mouse_y) and (mouse_y<(random_pos[1]+text_box[3])):
		text = font.render("Click this button to change color", True, BLUE)
		pygame.draw.line(screen, BLUE, (random_pos[0], random_pos[1] + text_box[3] + 1), (random_pos[0] + text_box[2], random_pos[1] + text_box[3] + 1))
	else:
		text = font.render("Click this button to change color", True, BLUE)


	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if (random_pos[0]<mouse_x) and (mouse_x<(random_pos[0]+text_box[2])) and (random_pos[1]<mouse_y) and (mouse_y<(random_pos[1]+text_box[3])):
					circle_color = (randint(0,255),randint(0,255),randint(0,255))
					circle_color_invert = (255 - circle_color[0], 255 - circle_color[1], 255 - circle_color[2])
					
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()
