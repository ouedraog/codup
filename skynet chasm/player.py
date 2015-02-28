#Solution of the Skynet:The Chasm by Juste Abel
import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

R = int(raw_input()) # the length of the road before the gap.
G = int(raw_input()) # the length of the gap.
L = int(raw_input()) # the length of the landing platform.

# game loop
gape_dist = R
instr = ""
speeds = []
while 1:
    S = int(raw_input()) # the motorbike's speed.
    X = int(raw_input()) # the position on the road of the motorbike.
    
    speeds.append(S)
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
     # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    gape_dist = R -X-1
    #case initial speed > G
    #case initial speed is < G 
    if(gape_dist <0):
        instr = "SLOW"
    elif(gape_dist < G):
        instr = "JUMP"
    elif(speeds[0]==G+1):
        instr = "WAIT"
    elif (speeds[0] > G+1):
        instr = "SLOW"
        if(S<=G+1): 
            instr = "WAIT"
    else:
        instr = "SPEED"
        if(S>G): 
            instr = "WAIT"
        
    print instr
        
