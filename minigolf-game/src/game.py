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

        Handles all the different event types that have an affect on the game.
        Calls all the methods required to move the ball etc.

        On a shot, the shot power is set to double the distance from the ball to the mouse position.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # a new shot can only be hit when the ball is stopped
                    if not self.x_speed and not self.y_speed:
                        self.handle_shot()
                        
            self.move_ball()
            self.water_hit()
            self.in_hole()

            self.field.all_elements.draw(self.display)
            self.ball_group.draw(self.display)
            
            pygame.display.update()
            
            self.clock.tick(60)

    def handle_shot(self):
        """A method to handle the shot. 
        
        Sets ball speed and shot power.
        The total trip needs to be reset on every shot in order to calculate the shot distance.
        """
        click_pos = pygame.mouse.get_pos()
        self.ball_x, self.ball_y = self.ball.rect.x, self.ball.rect.y
        self.x_speed = click_pos[0] - self.ball_x
        self.y_speed = click_pos[1] - self.ball_y
        self.shot_power = math.sqrt(
            self.x_speed**2+self.y_speed**2)*2
        self.total_trip = 0

    def move_ball(self):
        """A method that handles moving the ball.

        x and y coordinates change at different pace based on the shot coordinates.
        This achieves a linear movement for the ball across the field.
        The coordinates are updated based on the direction of the shot.
        If the ball has travelled enough, its speed will be zeroed.
        """
        self.x_moves += abs(self.x_speed)*100
        self.y_moves += abs(self.y_speed)*100

        wall_hit = self.field.check_wall_hits(self.ball)
        # water_hit = self.field.check_water_hits(self.ball)

        if wall_hit:
            self.x_speed = -self.x_speed
            self.y_speed = -self.y_speed

        if self.x_moves > 10000:
            if self.x_speed > 0:
                self.ball.rect.move_ip(1, 0)
            elif self.x_speed < 0:
                self.ball.rect.move_ip(-1, 0)
            self.x_moves = 0
            self.total_trip += 1
        if self.y_moves > 10000:
            if self.y_speed > 0:
                self.ball.rect.move_ip(0, 1)
            elif self.y_speed < 0:
                self.ball.rect.move_ip(0, -1)
            self.y_moves = 0
            self.total_trip += 1

        if self.total_trip >= self.shot_power:
            self.x_speed = 0
            self.y_speed = 0

    def in_hole(self):
        """A method to check if the hole ands the ball are colliding.

        Uses a circle ratio instead of the default rectangle.
        """
        in_hole = pygame.sprite.spritecollide(
            self.ball, self.field.holes, False, pygame.sprite.collide_circle_ratio(0.3))
        if in_hole:
            print('you won')
            sys.exit()
            
    def water_hit(self):
        water_hit = self.field.check_water_hits(self.ball)
        if water_hit:
            self.ball.rect.x = self.ball_x
            self.ball.rect.y = self.ball_y
            self.x_speed = 0
            self.y_speed = 0
        
