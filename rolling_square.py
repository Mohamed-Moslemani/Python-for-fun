import pygame,math,random
pygame.init()
screen_size = (600,600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Rolling Square with Colliding Balls")
WHITE = (255,255,255);BLUE = (0,0,255);RED = (255,0,0)
square_size=100;angle=0;angular_speed=2
num_balls=10;ball_radius=10;balls=[]
center_x, center_y = screen_size[0]//2, screen_size[1]//2
clock=pygame.time.Clock();running=True

for _ in range(num_balls):
    ball_angle=random.uniform(0,360)
    ball_speed = random.uniform(1,3)
    radius_offset=random.uniform(100,150)
    vx = random.choice([-1,1])*random.uniform(1,3)
    vy = random.choice([-1,1]) * random.uniform(1,3)
    balls.append({"angle":ball_angle,"speed":ball_speed,"radius_offset":radius_offset,
                  "vx":vx,"vy":vy,"x":center_x + radius_offset*math.cos(math.radians(ball_angle)),
                  "y":center_y + radius_offset*math.sin(math.radians(ball_angle))})

def check_collision(ball1,ball2):
    dx=ball1["x"]-ball2["x"]
    dy = ball1["y"] - ball2["y"]
    distance=math.sqrt(dx**2+dy**2)
    if distance<2*ball_radius:
        angle=math.atan2(dy, dx)
        speed1=math.sqrt(ball1["vx"]**2 + ball1["vy"]**2)
        speed2=math.sqrt(ball2["vx"]**2 + ball2["vy"]**2)
        ball1["vx"]=speed2 * math.cos(angle)
        ball1["vy"]=speed2 * math.sin(angle)
        ball2["vx"]=speed1*math.cos(angle+math.pi)
        ball2["vy"]=speed1*math.sin(angle+math.pi)

def check_ball_square_collision(ball, corners):
    for i in range(4):
        x1,y1=corners[i]
        x2, y2 = corners[(i+1)%4]
        dx,dy = x2 - x1, y2 - y1
        length=math.sqrt(dx**2+dy**2)
        nx,ny=dy/length,-dx/length
        proj_length = (ball["x"]-x1)*nx + (ball["y"] - y1)*ny
        if abs(proj_length) < ball_radius:
            vx_proj=ball["vx"]*nx + ball["vy"]*ny
            vy_proj=ball["vx"]*ny - ball["vy"]*nx
            ball["vx"]-=2*vx_proj*nx
            ball["vy"]-=2*vx_proj*ny
            break

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:running=False
    screen.fill(WHITE)
    corners=[]
    for i in range(4):
        theta=math.radians(angle + i*90)
        x=center_x + square_size/2 * math.cos(theta)
        y = center_y + square_size/2*math.sin(theta)
        corners.append((x,y))
    pygame.draw.polygon(screen,BLUE,corners)
    for i,ball in enumerate(balls):
        ball["x"]+=ball["vx"]
        ball["y"]+=ball["vy"]
        for j,other_ball in enumerate(balls[i+1:], start=i+1):
            check_collision(ball, other_ball)
        check_ball_square_collision(ball,corners)
        if ball["x"]<ball_radius or ball["x"]>screen_size[0] - ball_radius:
            ball["vx"]*=-1
        if ball["y"]<ball_radius or ball["y"]>screen_size[1]-ball_radius:
            ball["vy"]*=-1
        pygame.draw.circle(screen,RED,(int(ball["x"]),int(ball["y"])),ball_radius)
    angle+=angular_speed
    if angle>=360: angle -= 360
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
