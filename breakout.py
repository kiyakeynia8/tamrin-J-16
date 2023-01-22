import random
import arcade

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500,height=600,title= "breakout")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.me = Rocket(self.width//2,30,arcade.color.APPLE_GREEN,"kia")
        self.ball = Ball(self.width//2,30)
        self.squares = []
        self.sqr_x = 15
        self.sqr_y = 500
        self.a = 0
        
        for i in range(5):
            self.sqr_y -= 55
            for i in range(17):
                self.square = Square(self.sqr_x, self.sqr_y, arcade.color.RED)
                self.squares.append(self.square)
                self.sqr_x += 30

    def on_draw(self):
        arcade.start_render()
        self.me.draw()
        self.ball.draw()
        for square in self.squares:
            square.draw()
        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
        if self.me.width < x < self.width-self.me.width:
            self.me.center_x = x 

    def on_update(self, delta_time):
        self.ball.move()
  
        if self.ball.center_x < 15 or self.ball.center_x > self.width - 15:
            self.ball.change_x *= -1

class Rocket(arcade.Sprite):
    def __init__(self,x,y,c,n):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = c
        self.name = n
        self.change_x = 0
        self.change_y = 0
        self.width = 60
        self.height = 10
        self.speed = 4
        self.score = 0

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

class Ball(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = arcade.color.WHITE
        self.radius = 10
        self.change_x = random.choice([1,-1])
        self.change_y = 1
        self.speed = 1
        self.width = self.radius * 2
        self.height = self.radius * 2
    
    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

class Square(arcade.Sprite):
    def __init__(self,x,y,c):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = c
        self.change_x = 0
        self.change_y = 0
        self.width = 25
        self.height = 20

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

game = Game()
arcade.run()