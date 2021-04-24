import pygame

pygame.init()

display_width = 1000
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('машинка.png')
carImg2 = pygame.image.load('карта.png')
angle = 10
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def car2(x,y):
    gameDisplay.blit(carImg2, (x,y))



x =  (display_width * 0.5)
y = (display_height * 0.5)	#1
x2 =  (display_width * 0.5)
y2 = (display_height * 0.8)	#1
x_ball =(display_width * 0.45)
y_ball =(display_height * 0.4)
x_change = 0
y_change = 0
x2_change = 0
y2_change = 0
ball_x_change = 0
ball_y_change = 0
#spawn = False
car_speed = 0
car2_speed = 0
ball_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        
        ######################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                rotaded_image = pygame.transform.rotate(carImg, -angle)
                new_rect = rotated_image.get_rect(center = carImg.get.rect(center(x, y)).center)
            elif event.key == pygame.K_d:
                rotaded_image = pygame.transform.rotate(carImg, angle)
                new_rect = rotated_image.get_rect(center = carImg.get.rect(center(x, y)).center)
            elif event.key == pygame.K_w:
                y_change = -5
            elif event.key == pygame.K_s:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_change = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                y_change = 0
        ######################
    ##
    x += x_change
    y += y_change
    x2 += x2_change
    y2 += y2_change
    ##         
    gameDisplay.fill(white)

        
    car(x,y)
    car2(x2, y2)
   

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()