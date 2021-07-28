"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from campy.graphics.gobjects import GLabel
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 40 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    live = NUM_LIVES
    # Add animation loop here!
    # move
    dx = graphics.get_x_speed()
    dy = graphics.get_y_speed()
    score = 0
    while True:
        pause(FRAME_RATE)

    # check
        if graphics.game_start:
            graphics.ball.move(dx, dy)
        if graphics.ball.y >= graphics.window.height:
            graphics.game_start = False
            live -= 1
            if live > 0:
                graphics.reset_ball()
            else:
                graphics.reset_ball()
                score_label = GLabel('Score:' + str(score), x=150, y=400)
                score_label.font = '-30'
                graphics.window.add(score_label)
                break
        # ball meets walls
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            dx *= -1
        if graphics.ball.y <= 0:
            dy *= -1

        # ball meets objects
        if graphics.meets_object():
            score += graphics.meets_object()
            dy *= -1


if __name__ == '__main__':
    main()
