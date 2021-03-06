import math
import random


class BallHandler:
    """A class that handles ball movement on the field.

    Attributes:
        ball: The ball on the field.
        field: The actual field.
        x_dir:
            x direction and distance between ball and click position.
        y_dir:
            y direction and distance between ball and click position.
        x_float: Remainder x value from the shot distance.
        y_float: Remainder y value from the shot distance.
        total_trip:
            Used to determine the distance the ball has travelled.
        shot_power: Used to calculate the total shot distance.
        ball_x: x coordinate of the ball before each shot
        ball_y: y coordinate of the ball before each shot.
        hit_ranges: The wall coordinate ranges.
        shot_allowed: A new shot can only be made to a stationary ball.
        velocity: Determines the speed of the ball.
        counter: Used to count the shots.
    """

    def __init__(self, ball, field, walls, counter):
        """Initializes the needed variables for moving the ball.

        Args:
            ball: The ball at its initial coordinates
            field: A field generated by the Field class
            walls: The coordinates for the walls on the field
            counter: A counter generated by the ShotCounter class
        """
        self.ball = ball
        self.field = field
        self.x_dir = 0
        self.y_dir = 0
        self.x_float = 0.0
        self.y_float = 0.0
        self.total_trip = 0
        self.shot_power = 0
        self.ball_x, self.ball_y = self.ball.get_coordinates()
        self.hit_ranges = walls
        self.shot_allowed = True
        self.velocity = 100
        self.counter = counter

    def handle_shot(self, click_pos):
        """A method to handle the shot.

        Sets ball speed and shot power.
        The total trip needs to be reset on every shot
        in order to calculate the shot distance.

        Args:
            click_pos: Mouse coordinates on click.
        """
        if self.shot_allowed:
            self.ball_x, self.ball_y = self.ball.get_coordinates()
            self.x_dir = (click_pos[0] - (self.ball_x+6))
            self.y_dir = (click_pos[1] - (self.ball_y+6))
            self.shot_power = math.sqrt(
                self.x_dir**2+self.y_dir**2)*2
            self.total_trip = 0
            self.shot_allowed = False
            self.x_float = (abs(self.x_dir)/self.velocity -
                            abs(self.x_dir)//self.velocity)*100
            self.y_float = (abs(self.y_dir)/self.velocity -
                            abs(self.y_dir)//self.velocity)*100
            self.velocity = 100
            self.counter.plus_one()

    def move_ball(self):
        """A method that handles moving the ball.

        Moves the ball to the correct direction.
        Since the pygame rect object only handles integer values,
        the remainder values are handled separately.
        By choosing a random integer below 100,
        the ball moves correctly most of the time.
        """
        self.ball.move(self.x_dir/self.velocity,
                       self.y_dir/self.velocity)

        checker = random.randint(0, 100)
        if checker < self.x_float:
            if self.x_dir > 0:
                self.ball.move(1, 0)
            elif self.x_dir < 0:
                self.ball.move(-1, 0)
        if checker < self.y_float:
            if self.y_dir > 0:
                self.ball.move(0, 1)
            elif self.y_dir < 0:
                self.ball.move(0, -1)

        self.total_trip += max(abs(self.x_dir/self.velocity),
                               abs(self.y_dir/self.velocity))

        if self.total_trip >= self.shot_power or self.velocity < 1:
            self.x_dir = 0
            self.y_dir = 0
            self.x_float = 0.0
            self.y_float = 0.0
            self.shot_allowed = True

        self.water_hit()
        self.wall_hit()
        self.check_light_sand_hits()
        self.check_dark_sand_hits()

    def water_hit(self, test_helper=False):
        """A method to check if the ball is in water.

        If the ball hits water,
        it is returned to its starting position.

        Args:
            test_helper: Used for testing the class.
        """
        water_hit = self.field.check_water_hits(test_helper)
        if water_hit:
            self.ball.set_location(self.ball_x, self.ball_y)
            self.x_dir = 0
            self.y_dir = 0
            self.shot_allowed = True

    def wall_hit(self):
        """A method to bounce the ball off walls.

        Checks the outer walls separately.
        The walls inside the field are checked based on the coordinate
        ranges of the walls. The ranges are modified a bit to take into
        account the usage of the upper left coordinates of the ball.
        A range of wall is only checked if the direction of the ball
        allows the ball to hit the wall from that direction.
        One cell is 15x15 pixels and the ball is 13x13 pixels.
        """
        ball_x, ball_y = self.ball.get_coordinates()

        self.check_outer_walls(ball_x, ball_y)

        if self.x_dir < 0:
            for x_coord, ranges in self.hit_ranges['right'].items():
                if ball_x in range((x_coord+1)*15-2, (x_coord+1)*15):
                    self.switch_x_direction(ball_y, ranges)
        elif self.x_dir > 0:
            for x_coord, ranges in self.hit_ranges['left'].items():
                if ball_x in range((x_coord-1)*15+2, (x_coord-1)*15+4):
                    self.switch_x_direction(ball_y, ranges)

        if self.y_dir < 0:
            for y_coord, ranges in self.hit_ranges['bottom'].items():
                if ball_y in range((y_coord+1)*15-2, (y_coord+1)*15):
                    self.switch_y_direction(ball_x, ranges)
        elif self.y_dir > 0:
            for y_coord, ranges in self.hit_ranges['top'].items():
                if ball_y in range((y_coord-1)*15+2, (y_coord-1)*15+4):
                    self.switch_y_direction(ball_x, ranges)

    def check_outer_walls(self, ball_x, ball_y):
        """Manually checks if the ball hits the outer walls."""
        height, width = self.field.get_dimensions()

        if ball_x <= 15 and self.x_dir < 0:
            self.flip_x()
        if ball_x >= width-28 and self.x_dir > 0:
            self.flip_x()
        if ball_y <= 15 and self.y_dir < 0:
            self.flip_y()
        if ball_y >= height-28 and self.y_dir > 0:
            self.flip_y()

    def switch_y_direction(self, ball_x, ranges):
        """Checks if the ball hits a horizontal wall

        Args:
            x_range: A range of x coordinates that have walls on them
            ball_x: The x coordinate of the ball
        """
        for x_range in ranges:
            if ball_x in range((x_range[0]-1)*15+4, x_range[1]*15-4):
                self.flip_y()

    def switch_x_direction(self, ball_y, ranges):
        """Checks if the ball hits a vertical wall

        Args:
            y_range: A range of y coordinates that have walls on them
            ball_y: The x coordinate of the ball
        """
        for y_range in ranges:
            if ball_y in range((y_range[0]-1)*15+4, y_range[1]*15-4):
                self.flip_x()

    def flip_y(self):
        self.y_dir = -self.y_dir

    def flip_x(self):
        self.x_dir = -self.x_dir

    def check_light_sand_hits(self):
        """A method to change the ball speed when it hits light sand.

        x_float and y_float values are updated based on the velocity.
        """
        if self.field.check_light_sand_hits():
            self.velocity = 130
            self.total_trip += 3
        else:
            self.velocity = 100
        self.x_float = (abs(self.x_dir)/self.velocity -
                        abs(self.x_dir)//self.velocity)*100
        self.y_float = (abs(self.y_dir)/self.velocity -
                        abs(self.y_dir)//self.velocity)*100

    def check_dark_sand_hits(self):
        """A method to change the ball speed when it hits dark sand.

        x_float and y_float values are updated based on the velocity.
        """
        if self.field.check_dark_sand_hits():
            self.velocity = 150
            self.total_trip += 5
        else:
            self.velocity = 100
        self.x_float = (abs(self.x_dir)/self.velocity -
                        abs(self.x_dir)//self.velocity)*100
        self.y_float = (abs(self.y_dir)/self.velocity -
                        abs(self.y_dir)//self.velocity)*100
