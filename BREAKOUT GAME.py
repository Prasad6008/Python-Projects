import pygame

pygame.init()

#Colors:
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (60,160,200)
RED = (255,0,0)
GREEN = (57, 153, 24)

#Sizes:
WIDTH = 700
HEIGHT = 700
COLS = 10
ROWS = 6

#Frame per seconds:
FPS = 80

#Screen:
win = pygame.display.set_mode(size=(WIDTH,HEIGHT))
clock = pygame.time.Clock()

#Classes:
class Paddle():
    def __init__(self):
        self.width = int(WIDTH/COLS)
        self.height = 20
        self.x_pos = int(WIDTH/2) - (int(WIDTH/COLS))/2
        self.y_pos = HEIGHT - 30
        self.speed = 10#px
        self.box = pygame.Rect(self.x_pos,self.y_pos,self.width,self.height)

    def draw_paddle(self):
        pygame.draw.rect(win,WHITE,self.box)

    def move_paddle(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.box.left > 0:
            self.box.x -= self.speed

        if key[pygame.K_RIGHT] and self.box.right < WIDTH:
            self.box.x += self.speed

class Ball():
    def __init__(self,paddle_x,paddle_y):
        self.radius = 10#px
        self.x_pos = paddle_x
        self.y_pos = paddle_y - self.radius
        self.dx = 3
        self.dy = -3
        self.game_status = 0
        self.circle = pygame.Rect(self.x_pos,self.y_pos,self.radius*2,self.radius*2)

    def draw_ball(self):
        pygame.draw.circle(win,BLUE,(self.circle.x,self.circle.y),10)

    def move_ball(self):

        #Ball collision with paddle:
        if paddle.box.colliderect(self.circle) and self.dy > 0:
            bounce = pygame.mixer.Sound('bounce.wav')
            bounce.play()
            self.dy *= -1
            self.dx *= 1

        #bALL COLLISION ON BRICKS:
        all_done = True

        row_num = 0
        for row in bricks_wall.bricks:
            col_num = 0
            for br in row:
                if self.circle.colliderect(br):
                    hit = pygame.mixer.Sound('hit.wav')

                    #Ball collision direction on bricks:
                    if abs(self.circle.top - br.bottom) < 5 and self.dy < 0:
                        hit.play()
                        self.dy *= -1
                    if abs(self.circle.bottom - br.top) < 5 and self.dy > 0:
                        hit.play()
                        self.dy *= -1
                    if abs(self.circle.right - br.left) < 5 and self.dx < 0:
                        hit.play()
                        self.dx *= -1
                    if abs(self.circle.left - br.right) < 5 and self.dx > 0:
                        hit.play()
                        self.dx *= -1
                    
                    bricks_wall.bricks[row_num][col_num] = (0,0,0,0)

                if bricks_wall.bricks[row_num][col_num] != (0,0,0,0):
                    all_done = False
                col_num+=1
            row_num+=1

        if all_done:
            self.game_status = 1
        
        self.circle.x += self.dx
        self.circle.y += self.dy

        #Ball collision on the wall
        if self.circle.right > WIDTH:
            self.dx *= -1
            self.dy *= 1
        if self.circle.top   < 0:
            self.dy *= -1
            self.dx *= 1
        if self.circle.left  < 0:
            self.dx *= -1
            self.dy *= 1
        if self.circle.bottom > HEIGHT + 30:
            self.game_status = -1

        return self.game_status

class Bricks():
    def __init__(self):
        self.width = int(WIDTH/COLS)
        self.height = 30
        self.bricks = []

    def create_bricks(self):
        for row in range(ROWS):
            bricks_row = []
            for col in range(COLS):
                brick_x = col * self.width
                brick_y = row * self.height

                brick = pygame.Rect(brick_x,brick_y,self.width,self.height)
                bricks_row.append(brick)
            self.bricks.append(bricks_row)

    def draw_bricks(self):
        for row in self.bricks:
            for br in row:
                pygame.draw.rect(win,GREEN,br)
                pygame.draw.rect(win,BLACK,br,2)



#Objects for classes:
paddle = Paddle()
ball   = Ball(paddle.x_pos + int(paddle.width/2),paddle.y_pos)
bricks_wall = Bricks()
bricks_wall.create_bricks()


run = True

while run:
    win.fill(BLACK)
    clock.tick(FPS)

    paddle.draw_paddle()
    paddle.move_paddle()

    ball.draw_ball()
    game_status = ball.move_ball()

    bricks_wall.draw_bricks()

    if game_status == -1:
        font = pygame.font.SysFont(None, 80)
        text = font.render("GAME OVER",True,RED)
        text_dest = text.get_rect(center= (WIDTH/2,HEIGHT/2))
        win.blit(text,text_dest)
        pygame.display.update()
        pygame.time.delay(2000)
        run = False

    if game_status == 1:
        font = pygame.font.SysFont(None,90)
        text = font.render("***YOU WIN***",True,RED)
        text_dest = text.get_rect(center=(WIDTH/2,HEIGHT/2))
        win.blit(text,text_dest)
        pygame.display.update()
        pygame.time.delay(3000)
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
