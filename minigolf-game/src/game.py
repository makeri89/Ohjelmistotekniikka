import pygame


class Game:
    """A class for the loop running the game.

    Attributes:
        run: Starts the loop for the game.
    """

    def __init__(self, clock, field, display, renderer, ball_handler, counter):
        """Constructor that sets the required objects to run the game.

        Args:
            clock: Clock ticking enables the ball to be animated.
            field: Field class object that contains the elements of the field.
            display: Pygame display that has its size set already.
        """
        self.clock = clock
        self.field = field
        self.display = display
        self.counter = counter

        self.renderer = renderer
        self.ball_handler = ball_handler

    def run(self):
        """Loop that stops when manually exited or the ball goes to the hole.

        Handles all the different event types that have an affect on the game.
        Calls all the methods required to move the ball etc.

        On a shot, the shot power is set to double the distance from the ball to the mouse position.
        """
        running = True
        while running:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        # sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.ball_handler.handle_shot()
            except pygame.error as e:
                print(f'An error "{e}" occurred :(')
                running = False
                pygame.quit()

            self.ball_handler.move_ball()
            self.field.in_hole()

            self.renderer.render(self.counter.get_shots())
            self.clock.tick(120)
