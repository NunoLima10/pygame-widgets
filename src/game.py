from src.slider import Slider

import pygame as pg

class Game:
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
        return (self.window_width, self.window_height)
    
    @property
    def window_center(self) -> tuple:
        return (self.window_width // 2, self.window_height // 2)
    
    def setup(self) -> None:
        pg.init()
        pg.display.set_caption(self.title)
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode(self.window_size)


    def run(self) -> None:
        while True:
            self.clock.tick(self.fps)
            self.check_events()
            self.update()
            self.draw()

    def close(self) -> None:
        pg.quit()
        exit()

    def check_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.close()
            self.slider.mouse_trigger(event)

    def update(self) -> None:
        mouse_position = pg.mouse.get_pos()
        self.slider.update(mouse_position)

    def draw(self) -> None:
        self.screen.fill(self.default_background_color)
        self.slider.draw()
        pg.display.update()

    def start(self) -> None:
        self.slider = Slider(
            surface=self.screen,
            position=(20,20),
            size=(200,10),
            color=(255,255,255),
            start_position=0.1,
            label_text="label"
        )
        self.run()
