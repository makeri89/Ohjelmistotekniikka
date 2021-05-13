import pygame


class Game:
    """A class for the loop running the game.

    Attributes:
        clock: A pygame clock.
        display: A pygame display.
        counter: Used to count the shots.
        field: Sets the actual field for the game.
        renderer: Handles the rendering of pygame objects.
        ball_handler: Handles ball movement on the field.
        finished: Tells whether or not the game is finished.
    """

    def __init__(self, clock, display, renderer, ball_handler, counter, field):
        """Sets the required objects to run the game.

        Args:
            clock: Clock ticking enables the ball to be animated.
            display: Pygame display that has its size set already.
            renderer: Renders all objects on the display.
            ball_handler: Handles ball movement.
            counter: Counts the shots
            field (Field):
                Contains the elements of the field.
        """
        self.clock = clock
        self.display = display
        self.counter = counter
        self.field = field

        self.renderer = renderer
        self.ball_handler = ball_handler

        self.finished = False

    def run(self):
        """Fires up the main game loop.

        Stops when manually exited or the ball goes to the hole.
        Handles all the different event types that have an affect
        on the game. Calls all the methods required to move
        the ball etc. Exited variable is used to break out of
        the loop to prevent errors.

        Raises:
            pygame.error:
                On error prints the error message and exits.
        """
        exited = False
        while True:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exited = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.ball_handler.handle_shot(pygame.mouse.get_pos())
            except pygame.error as error_msg:
                print(f'An error "{error_msg}" occurred :(')
                pygame.quit()
                break
            if exited:
                break
            self.ball_handler.move_ball()
            self.renderer.render(self.counter.get_shots())
            if self.field.in_hole():
                pygame.quit()
                self.finished = True
                break
            self.clock.tick(120)
