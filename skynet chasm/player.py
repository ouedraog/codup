import sys, math

R = int(raw_input()) # the length of the road before the gap.
G = int(raw_input()) # the length of the gap.
L = int(raw_input()) # the length of the landing platform.

# game loop
gape_dist = R
instr = ""
while 1:
    S = int(raw_input()) # the motorbike's speed.
    X = int(raw_input()) # the position on the road of the motorbike.

    gape_dist = R -X-1 #The distance to the gap
    
    if(gape_dist <0): #slow after passing the gap
        instr = "SLOW"
    elif(gape_dist < G): #we are close to the gap => JUMP
        instr = "JUMP"
    elif(S==G+1): #we have reached the right speed so WAIT
        instr = "WAIT"
    elif (S > G+1): #We are going to fast so SLOW
        instr = "SLOW"
    else:
        instr = "SPEED" #Otherwise speed up
        
    print instr
        
