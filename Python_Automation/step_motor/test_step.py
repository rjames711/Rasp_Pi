from lib import Step
import curses
from threading import Thread

step_per_rev = 200
gear_ratio = 15.3
output_steps_per_rev = step_per_rev*gear_ratio
print "output steps per rev:" + str(output_steps_per_rev)

my_stepper= Step.Stepper(int(output_steps_per_rev))
cycling=False
cycles=0

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
stdscr.nodelay(1)

def adjust_rpm(rpm, adjustment):
    rpm+=adjustment
    if rpm>30:
        return 30
    elif rpm < 1:
        return 1
    else:
        return rpm

def manual_control():
    rpm=10
    global cycles
    global cycling
    x1=0
    x2=30
    y1=0
    y2=0
    thread=0
    
    headings_left=["'Q' to quit",
                   "",
         #     "USE ARROW KEYS TO CONTROL MOTOR POSITION AND SPEED",
              "Left:\tMove motor CCW",
              "Right:\tMove motor CW",
              "Up:\tIncrease motor speed",
              "Down:\tDecrease motor speed",
                "Enter:\tStart / Stop Cycling",
              "",
              ""]
    headings_right=["Page Up:\t  Move 45 deg forward",
                    "Page Down: Move 45 deg backward",
                    "Home:\t  Move to home position",
                    "End:\t  Move to end position",
                    "Insert:\t  Reset Home Position",
                    "Delete:\t  Reset End position"
                    "",
                    ""]
                    
                    
    
    for i in range(y1,len(headings_left)):
        stdscr.addstr(i+y1,1+x1,headings_left[i])
    for i in range(y2,len(headings_right)):
        stdscr.addstr(i+y2,1+x2,headings_right[i])
           
    stdscr.refresh()
    key = ''
    while key != ord('q') and key != ord('Q'):
        stdscr.addstr(i+2,1, "Motor Speed =\t"+str(rpm)+' rpm')
        stdscr.addstr(i+3,1, "End Position =\t"+str(my_stepper.end_position)+' degrees  ')
        stdscr.addstr(i+4,1, "Position =\t"+str(my_stepper.position)+' degrees  ')
        stdscr.addstr(i+5,1, "Count =\t"+str(cycles)+' cycles '+ str(cycling)+" ") 
        
        key = stdscr.getch()
        #stdscr.addch(20,25,key)
        stdscr.refresh()
        if key == curses.KEY_UP:
            rpm=adjust_rpm(rpm,1)            
        elif key == curses.KEY_DOWN:
            rpm=adjust_rpm(rpm,-1)            
        elif key== curses.KEY_LEFT:
            my_stepper.step_degrees(-1,rpm)
        elif key== curses.KEY_RIGHT:
            my_stepper.step_degrees(1,rpm)
        elif key== curses.KEY_HOME:
            my_stepper.go_to_position(0,rpm)
        elif key==curses.KEY_NPAGE:
            my_stepper.go_to_position(my_stepper.position-45,rpm)
        elif key==curses.KEY_PPAGE:
            my_stepper.go_to_position(my_stepper.position+45,rpm)
        elif key==curses.KEY_END:
            my_stepper.go_to_position(my_stepper.end_position,rpm)
        elif key == curses.KEY_IC:
            my_stepper.reset_home()
        elif key == curses.KEY_DC:
            my_stepper.reset_end()
        elif key == ord('s') or key == ord('S'):
            cycling = not cycling
        
        if cycling:
           cycle(rpm)
          
            



    curses.endwin()

def cycle(rpm):
    global cycles
    if my_stepper.position==0: #stepper is in home position
        my_stepper.go_to_position(my_stepper.end_position,rpm)
    else:
        my_stepper.go_to_position(0,rpm)
    cycles+=.5
        

manual_control()
