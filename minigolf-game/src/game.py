import pygame
from renderer import Renderer
from ball_handler import BallHandler


class Game:
    """A class for the loop running the game.

    Attributes:
        run: Starts the loop for the game.
    """

    def __init__(self, clock, field, display, renderer, ball_handler):
        """Constructor that sets the required objects to run the game.

        Args:
            ball: Ball sprite to be hit.
            clock: Clock ticking enables the ball to be animated.
            field: Field class object that contains the elements of the field.
            display: Pygame display that has its size set already.
        """
        self.clock = clock
        self.field = field
        self.display = display
        
        self.renderer = Renderer(self.display, self.field)
        self.ball_handler = BallHandler(self.field.get_ball(), self.field)

    def run(self):
        """Loop that stops when manually exited or the ball goes to the hole.

        Handles all the different event types that have an affect on the game.
        Calls all the methods required to move the ball etc.

        On a shot, the shot power is set to double the distance from the ball to the mouse position.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.ball_handler.handle_shot()

            self.ball_handler.move_ball()
            self.in_hole()

            self.renderer.render()
            self.clock.tick(60)

    def in_hole(self):
        """A method to check if the hole ands the ball are colliding.

        Uses a circle ratio instead of the default rectangle.
        """
        in_hole = pygame.sprite.spritecollide(
            self.field.get_ball(), self.field.get_holes(), False, pygame.sprite.collide_circle_ratio(0.3))
        if in_hole:
            print('you won')
            pygame.quit()