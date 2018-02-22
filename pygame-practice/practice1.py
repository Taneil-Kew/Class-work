import sys, pygame, random
pygame.init()

size = width, height = 800, 600
ballnum =50


black = 0, 0, 0

screen = pygame.display.set_mode(size)
balls=[]
speeds=[]

ball = pygame.image.load("intro_ball.gif")





for i in range(ballnum):

    ballrect = ball.get_rect()
    ballrect.left = random.randrange(0,width-100)
    ballrect.top = random.randrange(0,height-100)
    balls.append(ballrect)
    speed = [random.randrange(-1,2,2),random.randrange(-1,2,2)]
    speeds.append(speed)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    for i in range(ballnum):
        speed = speeds[i]
        balls[i] = balls[i].move(speed)

        if balls[i].left < 0 or balls[i].right > width:
            speed[0] = -speed[0]
        if balls[i].top < 0 or balls[i].bottom > height:
            speed[1] = -speed[1]

        speeds[i] = speed

        screen.blit(ball, balls[i])
    pygame.display.flip()



