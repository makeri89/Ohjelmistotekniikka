import sys
import math
import pygame


class Game:
    """A class for the loop running the game.

    Attributes:
        run: Starts the loop for the game.
    """

    def __init__(self, ball, clock, field, display):
        """Constructor that sets the required objects to run the game.

        Args:
            ball: Ball sprite to be hit.
            clock: Clock ticking enables the ball to be animated.
            field: Field class object that contains the elements of the field.
            display: Pygame display that has its size set already.
        """
        self.ball = ball
        self.clock = clock
        self.field = field
        self.display = display

        self.ball_group = pygame.sprite.Group()
        self.ball_group.add(self.ball)

        self.x_speed = 0
        self.y_speed = 0
        self.x_moves = 0
        self.y_moves = 0
        self.total_trip = 0
        self.shot_power = 0
        self.moves_amount = 0

    def run(self):
        """Loop that stops when manually exited or the ball goes to the hole.
        To be refactored.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ball.rect.move_ip(1, 0)
                    if event.key == pygame.K_DOWN:
                        self.ball.rect.move_ip(0, 1)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # a new shot can only be hit when the ball is stopped
                    if not self.x_speed and not self.y_speed:
                        click_pos = pygame.mouse.get_pos()
                        ball_x, ball_y = self.ball.rect.x, self.ball.rect.y
                        self.x_speed = click_pos[0] - ball_x
                        self.y_speed = click_pos[1] - ball_y
                        self.shot_power = math.sqrt(
                            self.x_speed**2+self.y_speed**2)*2
                        self.total_trip = 0

            self.x_moves += abs(self.x_speed)*100
            self.y_moves += abs(self.y_speed)*100

            if self.x_moves > 10000:
                if self.x_speed > 0:
                    self.ball.rect.move_ip(1, 0)
                if self.x_speed < 0:
                    self.ball.rect.move_ip(-1, 0)
                self.x_moves = 0
                self.total_trip += 1
            if self.y_moves > 10000:
                if self.y_speed > 0:
                    self.ball.rect.move_ip(0, 1)
                if self.y_speed < 0:
                    self.ball.rect.move_ip(0, -1)
                self.y_moves = 0
                self.total_trip += 1

            if self.total_trip >= self.shot_power:
                self.x_speed = 0
                self.y_speed = 0

            in_hole = pygame.sprite.spritecollide(
                self.ball, self.field.holes, False, pygame.sprite.collide_circle_ratio(0.3))

            if in_hole and abs(self.x_speed) < 20 and abs(self.y_speed) < 20:
                print('you won')
                sys.exit()

            self.field.all_elements.draw(self.display)
            self.ball_group.draw(self.display)

            pygame.display.update()

            self.clock.tick(60)
