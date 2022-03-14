#Poke the Dots Version 4
from uagame import Window
from random import randint
from pygame import QUIT, Color, MOUSEBUTTONUP
from pygame.time import Clock, get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

#user definied functions
def main():
    game = Game()
    game.play()
    
#user definied classes
class Game:
    # An object in this class represents a complete game
    # window,frame_rate,close_selected,clock,small_dot,big_bot,score
    def __init__(self):
        # Initialize a Game
        self._window = Window('Poke the Dots', 500, 400)
        self._adjust_window()
        self._frame_rate = 90  # larger is faster game
        self._close_selected = False
        self._clock = Clock()
        self._small_dot = Dot('red', [50,75], 30, [1,2], self._window)
        self._big_dot = Dot('blue', [200,100], 40, [2,1], self._window)
        self._small_dot.randomize()
        self._big_dot.randomize()
        self._score = 0        
    
    def _adjust_window(self):
        # Adjust the window for the game        
        self._window.set_font_name('ariel')
        self._window.set_font_size(64)
        self._window.set_font_color('white')
        self._window.set_bg_color('black')
    
    def play(self):
        # Play game until player presses close icon 
        # then close window
        while not self._close_selected:
            # play frame
            self.handle_events()
            self.draw()
            self.update()
        self._window.close()
    
    def handle_events(self):
        # Handle current game events by changing game
        # state appropriately
        event_list = get_events()
        for event in event_list:
            self.handle_one_event(event)
            
    def handle_one_event(self, event):
        #Handle one event by changing the game state appropriately
        if event.type == QUIT:
            self._close_selected = True
        elif event.type == MOUSEBUTTONUP:
            self.handle_mouse_up(event)

    def handle_mouse_up(self, event):
        # Respond to player releasing mouse button
        self._small_dot.randomize()
        self._big_dot.randomize()

    def draw(self):
        # Draw all game objects
        self._window.clear()
        self.draw_score()
        self._small_dot.draw()
        self._big_dot.draw()
        self._window.update()

    def update(self):
        # Update all game objects with state changes
        # that are not due to user events
        self._small_dot.move()
        self._big_dot.move()
        self._clock.tick(self._frame_rate)
        self._score = get_ticks() // 1000

    def draw_score(self):
        # Draw the time since the game began as a score
        string = 'Score: ' + str(self._score)
        self._window.draw_string(string, 0, 0)

class Dot:
    # object here represents a colored circle that can move
    # self,color,center, radius,velocity, window
    def __init__(self, color, center, radius, velocity, window):
        # Initialize a Dot
        self._color = color
        self._center = center
        self._radius = radius
        self._velocity = velocity
        self._window = window

    def move(self):
        # Change location and velocity of the Dot so it
        # remains on surface by bouncing from its edges
        size = (self._window.get_width(), self._window.get_height())
        for index in range(0, 2):
            # update center at index
            self._center[index] = self._center[index] + self._velocity[index]
            # dot perimeter outside window?
            if (self._center[index] < self._radius) or (self._center[index] + self._radius > size[index]):
                # change direction
                self._velocity[index] = - self._velocity[index]

    def draw(self):
        # Draw the dot on the surface
        surface = self._window.get_surface()
        color = Color(self._color)
        draw_circle(surface, color, self._center, self._radius)

    def randomize(self):
        # Change dot so that its center is at a random
        # point on the surface. Ensure that no part of a dot
        # extends beyond the surface boundary
        size = (self._window.get_width(), self._window.get_height())
        for index in range(0, 2):
            self._center[index] = randint(self._radius, size[index] - self._radius)

main()