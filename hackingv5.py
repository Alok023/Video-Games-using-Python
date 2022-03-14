#hacking version 5
from uagame import Window
from time import sleep

#create window
window = Window('Hacking',600,500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')

#font height & attempts
pause = 0.3
hgt = window.get_font_height()
y = 0
x = 0
tryleft = 4

#header = 2 content lines and 1 blank line
header = ['DEBUG MODE',str(tryleft)+' ATTEMPT(S) LEFT','']
for header_line in header:
    window.draw_string(header_line,x,y)
    window.update()
    sleep(pause)
    y += hgt    

#display paswd list
password = ['PROVIDE','SETTING','CANTINA','CUTTING','HUNTERS','SURVIVE','HEARING','HUNTING','REALIZE','NOTHING','OVERLAP','FINDING','PUTTING','']
for paswd in password:
    window.draw_string(paswd,x,y)
    window.update()
    sleep(pause)
    y += hgt

#select password
crt_paswd = password[7]

#lockout parameters
warning = '*** LOCKOUT WARNING ***'
x_warn = window.get_width() - window.get_string_width(warning)
y_warn = window.get_height() - window.get_font_height()

#attempts 
while tryleft > 0:
    guess = window.input_string('ENTER PASSWORD >',x,y)
    tryleft -= 1
    y += hgt
    if guess == crt_paswd:
        break
    else:
        if tryleft > 0:
            window.draw_string(str(tryleft),x,hgt)
    if tryleft == 1:
        window.draw_string(warning,x_warn,y_warn)

#clear window
window.clear()

#output screen prameters
x_space = window.get_width() - window.get_string_width(guess)
xmid = x_space // 2
y_hgt = 7 * hgt
y_space = window.get_height() - y_hgt
ymid = y_space // 2

#outcome lines 
if guess == crt_paswd:
    outcome = [guess,'','EXITING DEBUG MODE','','LOGIN SUCCESSFUL - WELCOME BACK','','PRESS ENTER TO CONTINUE']
else:
    outcome = [guess,'','LOGIN FAILURE - TERMINAL LOCKED','','PLEASE CONTACT AN ADMINISTRATOR','','PRESS ENTER TO EXIT']
#failure outcome = 4 lines + 3 blank lines
num = 0
for outcome_line in outcome:
    num += 1
    if num == 7:
        break
    window.draw_string(outcome_line,xmid,ymid)
    window.update()
    sleep(pause)
    ymid += hgt
    x_space = window.get_width()-window.get_string_width(outcome[num])
    xmid = x_space // 2

x_space = window.get_width()-window.get_string_width(outcome[6])
xmid = x_space // 2
window.input_string(outcome[6],xmid,ymid)

#window close
window.close()