import pygame,math,random
pygame.init()
screen_size = (600,600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Rolling Square with Rotating Balls")
WHITE = (255,255,255);BLUE = (0,0,255);RED = (255,0,0)
square_size = 100;angle = 0;angular_speed = 2
num_balls = 10;ball_radius = 10;balls = []
for _ in range(num_balls):
    ball_angle = random.uniform(0,360)
    ball_speed = random.uniform(1,3)
    radius_offset = random.uniform(100,150)
    balls.append({"angle":ball_angle,"speed":ball_speed,"radius_offset":radius_offset})
center_x,center_y = screen_size[0]//2,screen_size[1]//2
clock = pygame.time.Clock();running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:running = False
    screen.fill(WHITE)
    corners = []
    
    for i in range(4):
        theta = math.radians(angle+i*90)
        x = center_x+square_size/2*math.cos(theta)
        y = center_y+square_size/2*math.sin(theta)
        corners.append((x,y))
    pygame.draw.polygon(screen,BLUE,corners)
    for ball in balls:
        ball["angle"] += ball["speed"]
        if ball["angle"] >= 360:ball["angle"] -= 360
        ball_x = center_x+ball["radius_offset"]*math.cos(math.radians(ball["angle"]))
        ball_y = center_y+ball["radius_offset"]*math.sin(math.radians(ball["angle"]))
        pygame.draw.circle(screen,RED,(int(ball_x),int(ball_y)),ball_radius)
    angle += angular_speed
    
    
    if angle >= 360:angle -= 360
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
