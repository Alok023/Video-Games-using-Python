#Poke the Dots Version 3
from uagame import Window
from random import randint
from pygame import QUIT, Color, MOUSEBUTTONUP
from pygame.time import Clock, get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

#user definied functions
def main():
    window = create_window()
    game = create_game(window)
    play_game(game)
    window.close()

def create_window():
    # Create window, open it and return it
    window = Window('Poke the Dots', 500, 400)
    window.set_font_name('ariel')
    window.set_font_size(64)
    window.set_font_color('white')
    window.set_bg_color('black')
    return window  

def create_game(window):
    # Create a Game object for Poke the Dots.
    game = Game()
    game.window = window
    game.frame_rate = 90 # higher is faster
    game.close_selected = False
    game.clock = Clock()
    game.small_dot = create_dot('red', [50,75], 30, [1,2], window)
    game.big_dot = create_dot('blue', [200,100], 40, [2,1], window)
    randomize_dot(game.small_dot)
    randomize_dot(game.big_dot)
    game.score = 0    
    return game

def create_dot(color, center, radius, speed, window):
    # Create a Dot object for Poke the Dots
    dot = Dot()
    dot.color = color
    dot.center = center
    dot.radius = radius
    dot.velocity = speed
    dot.window = window
    return dot

def play_game(game):
    # Play game until the player presses the close icon
    while not game.close_selected:
        # play frame
        handle_events(game)
        draw_game(game)
        update_game(game)

def handle_events(game):
    # Handle the current game events.
    # Return True if the player clicked the close icon
    event_list = get_events()
    for event in event_list:
        # handle one event
        if event.type == QUIT:
            game.close_selected = True
        elif event.type == MOUSEBUTTONUP:
            handle_mouse_up(game)            

def handle_mouse_up(game):
    # Respond to player releasing mouse button
    randomize_dot(game.small_dot)
    randomize_dot(game.big_dot)

def draw_game(game):
    # Draw all game objects.
    game.window.clear()
    draw_score(game)    
    draw_dot(game.small_dot)
    draw_dot(game.big_dot)
    game.window.update()

def draw_score(game):
    # Draw the time since the game began as score    
    string = 'Score: ' + str(game.score)
    game.window.draw_string(string, 0, 0)

def update_game(game):
    # Update all game objects with state changes
    # that are not due to user events
    move_dot(game.small_dot)
    move_dot(game.big_dot)
    game.clock.tick(game.frame_rate)
    game.score = get_ticks() // 1000

def draw_dot(dot):
    # Draw the dot on the window.
    surface = dot.window.get_surface()
    color = Color(dot.color)
    draw_circle(surface, color, dot.center, dot.radius)

def move_dot(dot):
    # Change location and velocity of the dot so it
    # remains on the surface by bouncing from its edges
    size = (dot.window.get_width(), dot.window.get_height())
    for index in range(0, 2):
        # update center at index
        dot.center[index] = dot.center[index] + dot.velocity[index]
        # dot edge outside window?
        if (dot.center[index] < dot.radius) or (dot.center[index] + dot.radius > size[index]):
            # change direction
            dot.velocity[index] = - dot.velocity[index]

def randomize_dot(dot):
    # Change the dot so that its center is at a random point
    # Ensure that no part of a dot extends beyond the surface
    size = (dot.window.get_width(), dot.window.get_height())
    for index in range(0, 2):
        dot.center[index] = randint(dot.radius, size[index] - dot.radius)

class Game:
    # An object in this class represents a complete game
    # window,frame_rate,close_selected,clock,small_dot,big_bot,score
    pass

class Dot:
    # object here represents a colored circle that can move
    # color,center, radius,velocity, window
    pass

main()