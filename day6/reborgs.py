def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def sag_acik():
    if not front_is_clear() and right_is_clear():
        turn_right()
        move()
        turn_right()
        move()      
def sol_acik():
    if not front_is_clear() and not right_is_clear():
        turn_left()
def on_sag_acik():
    if front_is_clear()and right_is_clear():
        turn_right()
        move()
        turn_right()
        move()       
def on_sag_dacik():
    if front_is_clear()and not right_is_clear():
        move()
while not at_goal():
     on_sag_dacik()
     sol_acik()
     on_sag_acik()
     sag_acik()   

     
    
        
     
  
        
    
        
     
    
    
    
    