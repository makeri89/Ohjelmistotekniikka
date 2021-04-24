import pygame


class Game:
    """A class for the loop running the game.

    Attributes:
        run: Starts the loop for the game.
    """

    def __init__(self, clock, display, renderer, ball_handler, counter, field):
        """Constructor that sets the required objects to run the game.

        Args:
            clock: Clock ticking enables the ball to be animated.
            field: Field class object that contains the elements of the field.
            display: Pygame display that has its size set already.
        """
        self.clock = clock
        self.display = display
        self.counter = counter
        self.field = field

        self.renderer = renderer
        self.ball_handler = ball_handler

        self.finished = False

    def run(self):
        """Loop that stops when manually exited or the ball goes to the hole.

        Handles all the different event types that have an affect on the game.
        Calls all the methods required to move the ball etc.
        Exited variable is used to break out of the loop to prevent errors.

        Raises:
            pygame.error:
                If pygame encounters an error, the error message is printed and the game quits
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
