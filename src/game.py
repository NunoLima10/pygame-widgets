
import pygame as pg
import time

class Game:
    """
    A class to represent a game object

    Examples:
        from game import Game

        game = Game("MyGame",800,800)
        game.start()
    
    """
    def __init__(self, title: str, window_width: int, window_height: int, fps: int = 30) -> None:
        self.title =  title
        self.window_width = window_width
        self.window_height = window_height
        self.fps = fps

        # default
        self.default_background_color = (64,64,64)

        self.setup()
    
    @property
    def window_size(self) -> tuple:
        """
        Returns a tuple with the dimensions of the screen

        Examples:
            self.screen = pg.display.set_mode(self.window_size)

        """
        return (self.window_width, self.window_height)
    
    @property
    def window_center(self) -> tuple:
        """
        Returns a tuple with the x and y position of the center of the screen
        
        Examples:
            self.player.move_to(self.window_center)

        """
        return (self.window_width // 2, self.window_height // 2)
    
    def setup(self) -> None:
        """
        Initializes pygame and creates the game window

        Examples:
            self.game_map = load_game_map()

        """
        pg.init()
        pg.display.set_caption(self.title)
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(self.window_size)

        # <== YOUR SETUP CODE ==>

    def close(self) -> None:
        """
        Closes pygame and ends the execution of the program

        Examples:
            self.save_game_config()

        """
        # <== YOUR CLOSE CODE ==>

        pg.quit()
        exit()

    def run(self) -> None:
        """
        Start the game loop and calculates delta time

        """
        previous_time = time.time()

        while True:
            self.clock.tick(self.fps)
            now = time.time()
            delta_time = previous_time - now
            previous_time = now

            self.check_events()
            self.update(delta_time)
            self.draw()


    def check_events(self) -> None:
        """
        Checks all events in the application

        Examples:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.move_up() 

        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.close()

            # <== YOUR EVENT CODE ==>

    def update(self, delta_time: float) -> None:
        """
        Updating every frame of the game

        Look up information on frame independence if you don't know how to use delta time

        Args:
            delta_time (float): use to make frame rate independent

        Examples:
            self.player.position_x += 300 * delta_time

        """
        # <== YOUR UPDATE CODE ==>

        pass

    def draw(self) -> None:
        """
        Refreshes the game screen every frame of the game

        Used to call draw functions for game object

        Examples:
            self.player.draw(self.screen)
            
        """
        self.screen.fill(self.default_background_color)

        # <== YOUR DRAW CODE ==>

        pg.display.update()

    def start(self) -> None:
        """
        Initialization of game objects before starting the game

       Examples:
            self.player = Player(
                position=(0,0), 
                color=(255,0,0)
            )
        """
        # <== YOUR START CODE ==>
        
        self.run()
