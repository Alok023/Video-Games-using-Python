#hacking version 7
from uagame import Window
from time import sleep
from random import randint, choice
def main():
    location = [0,0]
    attempts = 4
    window = create_window()
    display_header(window, location, attempts)
    password = display_password_list(window, location)
    guess = get_guesses(window, password, location, attempts)
    end_game(window, guess, password)

def create_window():
    #create window, open and run 
    window = Window('Hacking',600,500)
    window.set_font_name('couriernew')
    window.set_font_size(18)
    window.set_font_color('green')
    window.set_bg_color('black')
    return window

def display_header(window, location, attempts):
    #display header = 2 content lines and 1 blank line
    #location is x any co-ordinates in a list format
    header = ['DEBUG MODE',str(attempts)+' ATTEMPT(S) LEFT','']
    for header_line in header:
        display_line(window, header_line, location)

def display_password_list(window, location):
    enbedded_size = 20    
    #display embedded paswd list
    password_list = ['PROVIDE','SETTING','CANTINA','CUTTING','HUNTERS','SURVIVE','HEARING','HUNTING','REALIZE','NOTHING','OVERLAP','FINDING','PUTTING']
    for password in password_list:
        password_line = embed_password(password, enbedded_size)
        display_line(window, password_line, location)
    #display blank line
    display_line(window, '', location)
    #set password
    return password_list[7]

def embed_password(password, size):
    #embed the password with random symbols
    fill = '!@#$%^*()-+=~[]{}'
    password_size = len(password)
    embedding = ''
    split_index = randint(0, size - password_size)
    for index in range (0, split_index):
        embedding += choice(fill)
    embedding += password
    for index in range (split_index + password_size, size):
        embedding += choice(fill)
    return embedding

def get_guesses(window, password, location, attempts_left):
    #attempts for password and return final guess
    prompt = 'ENTER PASSWORD >'
    hint_location = [window.get_width() // 2, 0]
    x_line = 0
    guess = prompt_user(window, prompt, location)
    attempts_left -= 1
    while guess != password and attempts_left > 0:
        #get the next guess
        window.draw_string(str(attempts_left),x_line,window.get_font_height())
        display_hint(window, password, guess, hint_location)
        check_warning(window, attempts_left)
        guess = prompt_user(window, prompt, location)
        attempts_left -= 1
    return guess

def check_warning(window, attempts_left):
    # check if 1 attempmt remaining and give warning if yes
    warning = '*** LOCKOUT WARNING ***'
    if attempts_left == 1:
        warning_x = window.get_width() - window.get_string_width(warning)
        warning_y = window.get_height() - window.get_font_height()
        window.draw_string(warning,warning_x,warning_y)

def display_hint(window, password, guess, location):
    #display hint in case of incorrect guess
    string = guess + ' INCORRECT'
    display_line(window, string, location)
    index = 0
    correct = 0
    total = len(password)
    #check matching letters in password
    for letter in guess:
        if index < total and letter == password[index]:
            correct += 1
        index += 1
    string = str(correct) + '/' + str(total) + ' IN MATCHING POSITIONS'
    display_line(window, string, location)

def end_game(window, guess, password):
    #clear screen
    window.clear()
    #get output parameters
    #    success
    if guess == password:
        outcome = [guess,'','EXITING DEBUG MODE','','LOGIN SUCCESSFUL - WELCOME BACK','']
        prompt = 'PRESS ENTER TO CONTINUE'
    #    failure
    else:
        outcome = [guess,'','LOGIN FAILURE - TERMINAL LOCKED','','PLEASE CONTACT AN ADMINISTRATOR','']
        prompt = 'PRESS ENTER TO EXIT'
    location = display_outcome(window, outcome)
    #prompt for end
    location[0] = (window.get_width() - window.get_string_width(prompt)) // 2
    prompt_user(window, prompt, location)
    #close window
    window.close()
    
def display_outcome(window, outcome):
    #display outcome
    #    get y co-ordinate
    string_height = window.get_font_height()
    outcome_height = (len(outcome) + 1) * string_height
    y_space = window.get_height() - outcome_height
    y_line = y_space // 2
    location = [0, y_line]
    for outcome_line in outcome:
        #    get x co-ordinate
        x_space = window.get_width() - window.get_string_width(outcome_line)
        location[0] = x_space // 2
        display_line(window, outcome_line, location)
    return location

def display_line(window, string, location):
    #display string and update location
    pause = 0.3
    window.draw_string(string, location[0], location[1])
    window.update()
    sleep(pause)
    location[1] += window.get_font_height()
    
def prompt_user(window, prompt, location):
    #get prompt for either input or ending program
    get_input = window.input_string(prompt, location[0], location[1])
    location[1] += window.get_font_height()
    return get_input

main()
