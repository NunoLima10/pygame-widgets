
from collections import  namedtuple
import pygame as pg

Position = namedtuple("position","x y")
Size = namedtuple("size","width height")
Color = namedtuple("Color", "r g b")

class Slider:
  def __init__(self, surface: pg.Surface, position: tuple, size: tuple, color: tuple, 
              start_position: float = 0, label_text: str = "") -> None:
    
    self.surface = surface

    #border
    self.position = Position(*position) 
    self.size = Size(*size) 
    self.border_color = color
    self.border_width = 1
    self.border_radius = 3

    # #swiper
    self.swiper_percentage = start_position
    self.swiper_precision = 2
    self.swiper_radius = self.size.height
    self.swiper_on_focus_radius = self.swiper_radius + 2
    self.swiper_position = self.get_swiper_position()
    self.swiper_color = Color(255,255,255)
    self.swiper_on_focus_color = Color(0,255,0)
    self.swiper_over_color = Color(255,0,0)

    #fill
    self.fill_position = self.position
    self.fill_size = Position(self.swiper_position.x - self.position.x, self.size.height)
    self.fill_color = Color(255,255,255)
    
    #label 
    self.label_text = label_text
    self.label_size = 25
    self.label_margin = 15
    self.label_is_visible = True
    self.label_font = "monospace"
    self.label_color = Color(255,255,255)
    
    #state
    self.over = False
    self.on_focus = False
  
  @property
  def rect(self) -> tuple:
    return (self.position, self.size)
  
  @property
  def fill_rect(self) -> tuple:
    return (self.fill_position, self.fill_size)
  
  def get_swiper_percentage(self) -> float:
    return self.swiper_percentage  
  
  def get_swiper_position(self) -> Position:
    x_position = self.position.x - self.swiper_radius + self.size.width * self.swiper_percentage
    y_position = self.position.y + self.size.height / 2
    return Position(x_position, y_position)

  def mouse_trigger(self, event) -> None: 
      if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        if self.on_focus: 
          self.over = True
        
      if event.type == pg.MOUSEBUTTONUP and event.button == 1:
        self.over = False

  def is_on_focus(self, position) -> bool:
    position = Position(*position)
    deltaX = (self.swiper_position.x - position.x) ** 2
    deltaY = (self.swiper_position.y - position.y) ** 2
    self.on_focus = self.swiper_radius > (deltaX + deltaY) ** 0.5

  def set_swiper_position(self, position) -> None:
    mouse_position = Position(*position)
    if self.over:
      if mouse_position.x <= self.position.x + self.size.width and mouse_position.x >= self.position.x:
        self.swiper_position = Position(mouse_position.x, self.swiper_position.y)
        self.fill_size = (self.swiper_position.x -self.position.x, self.size.height)

  def draw_label(self) -> None:
    font = pg.font.SysFont(self.label_font, self.label_size)
    text = font.render(f"{self.swiper_percentage} {self.label_text}",1, self.label_color)
    text_rect = text.get_rect()
    text_rect.topleft = (self.position.x + self.size.width + self.label_margin, self.size.height)
    self.surface.blit(text, text_rect)

  def get_swiper_color(self) -> Color:
    if self.over:
      return self.swiper_over_color

    if self.on_focus:
      return self.swiper_on_focus_color

    return self.swiper_color

  def draw(self) -> None:
    swiper_color = self.get_swiper_color()
    radius =  self.swiper_on_focus_radius if self.on_focus  else self.swiper_radius
    
    pg.draw.rect(self.surface, self.border_color, self.rect, self.border_width, self.border_radius)
    pg.draw.rect(self.surface, self.fill_color,self.fill_rect ,0, self.border_radius)
    pg.draw.circle(self.surface, swiper_color, self.swiper_position, radius) 
    
    if self.label_is_visible: 
      self.draw_label()

  def update_swiper_percentage(self) -> None:
    percentage = (self.swiper_position.x - self.position.x - self.size.width  / self.size.width ) / self.size.width
    percentage = 1 if percentage > 0.940 else  percentage
    percentage = 0 if percentage < 0.05 else  percentage
    self.swiper_percentage = round(percentage, self.swiper_precision)

  def update(self, mouse_position) -> None:
    self.is_on_focus(mouse_position)
    self.set_swiper_position(mouse_position)
    self.update_swiper_percentage()
    self.draw()
  
