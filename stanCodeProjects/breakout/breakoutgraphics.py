"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.ball_radius = ball_radius

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width-paddle_width)//2, y=self.window.height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window.width-ball_radius)//2, y=(self.window.height-ball_radius)//2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dy = 0
        self.__dx = 0
        self.set_ball_velocity()

        # Draw bricks
        for i in range(0, self.brick_cols+1):
            for j in range(0, self.brick_rows+1):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.color = self.color(j)
                self.brick.fill_color = self.color(j)
                self.window.add(self.brick, x=i*(self.brick.width+self.brick_spacing), y=self.brick_offset+j*(self.brick.height+self.brick_spacing))
        # Initialize our mouse listeners
        onmouseclicked(self.handle_click)
        self.game_start = False

        # score keeping
        # self.score = 0

        # meets object
    def meets_object(self):
        score = 0
        p1 = self.window.get_object_at(self.ball.x, self.ball.y)
        p2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        p3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        p4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        point = p1
        if point is None:
            point = p2
        if point is None:
            point = p3
        if point is None:
            point = p4
        if point is None:
            return False
        elif point is not self.paddle:
            self.window.remove(point)
            score += 1
            return score
        elif point is self.paddle:
            return True

    # getters
    def get_x_speed(self):
        return self.__dx

    def get_y_speed(self):
        return self.__dy

    # decide brick color
    @staticmethod
    def color(num_row):
        if num_row < 2:
            return 'red'
        elif 2 <= num_row < 4:
            return 'orange'
        elif 4 <= num_row < 6:
            return 'yellow'
        elif 6 <= num_row < 8:
            return 'green'
        else:
            return 'blue'

    def handle_click(self, e):
        self.game_start = True
        onmousemoved(self.handle_move)

    def handle_move(self, event):
        pdy = 0
        if event.x+self.paddle.width//2 >= self.window.width:
            pdx = self.window.width-self.paddle.width-self.paddle.x
            self.paddle.move(pdx, pdy)
        elif event.x-self.paddle.width//2 <= 0:
            pdx = 0-self.paddle.x
            self.paddle.move(pdx, pdy)
        else:
            pdx = event.x - self.paddle.width // 2 - self.paddle.x
            self.paddle.move(pdx, pdy)

    def reset_ball(self):
        self.ball.x = (self.window.width - self.ball_radius) // 2
        self.ball.y = (self.window.height - self.ball_radius) // 2
        self.window.add(self.ball)

    def set_ball_velocity(self):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randrange(0, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx *= -1


