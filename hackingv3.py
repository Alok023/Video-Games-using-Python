#hacking version 3
from uagame import Window
from time import sleep
#create window
window = Window('Hacking',600,500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')
#font height
hgt = window.get_font_height()
y = 0
#header = 2 content lines and 1 blank line
window.draw_string('DEBUG MODE',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('1 ATTEMPT(S) LEFT',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('',0,y)
window.update()
sleep(0.3)
y += hgt
#display paswd list
window.draw_string('PROVIDE',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('SETTING',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('CANTINA',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('CUTTING',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('HUNTERS',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('SURVIVE',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('HEARING',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('HUNTING',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('REALIZE',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('NOTHING',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('OVERLAP',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('FINDING',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('PUTTING',0,y)
window.update()
sleep(0.3)
y += hgt
window.draw_string('',0,y)
window.update()
sleep(0.3)
y += hgt
#prompt for password
guess = window.input_string('ENTER PASSWORD >',0,y)
#clear window
window.clear()
#output screen prameters
x_space = window.get_width() - window.get_string_width(guess)
xmid = x_space // 2
y_hgt = 7 * hgt
y_space = window.get_height() - y_hgt
ymid = y_space // 2
#outcome lines 
if guess == 'HUNTING':
    outcome_l2 = 'EXITING DEBUG MODE'
    outcome_l3 = 'LOGIN SUCCESSFUL - WELCOME BACK'
    outcome_l4 = 'PRESS ENTER TO CONTINUE'
else:
    outcome_l2 = 'LOGIN FAILURE - TERMINAL LOCKED'
    outcome_l3 = 'PLEASE CONTACT AN ADMINISTRATOR'
    outcome_l4 = 'PRESS ENTER TO EXIT'
#failure outcome = 4 lines + 3 blank lines
window.draw_string(guess,xmid,ymid)
window.update()
sleep(0.3)
ymid += hgt
window.draw_string('',0,ymid)
window.update()
sleep(0.3)
ymid += hgt
x_space = window.get_width() - window.get_string_width(outcome_l2)
xmid = x_space // 2
window.draw_string(outcome_l2,xmid,ymid)
window.update()
sleep(0.3)
ymid += hgt
window.draw_string('',0,ymid)
window.update()
sleep(0.3)
ymid += hgt
x_space = window.get_width() - window.get_string_width(outcome_l3)
xmid = x_space // 2
window.draw_string(outcome_l3,xmid,ymid)
window.update()
sleep(0.3)
ymid += hgt
window.draw_string('',0,ymid)
window.update()
sleep(0.3)
ymid += hgt
x_space = window.get_width() - window.get_string_width(outcome_l4)
xmid = x_space // 2
window.input_string(outcome_l4,xmid,ymid)
#window close
window.close()