from turtle import Turtle

STARTING_POSTION=[(0,0), (-20,0), (-40,0)]#this is a tuple AND A CONSTANT
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    
    def __init__(self):##what would happen if you intilaise a new snake object
        self.segment=[] #Create a variable called segment that belongs to this Snake object.
        self.create_snake()
        self.head=self.segment[0]#means the head the snake
        
        
    def create_snake(self):
        #creating the snake body
        ##another way to make 3 turtles
        for position in STARTING_POSTION:#creates the 3 squares the starting snake
            self.add_segment(position)#calls in the add segment
            
            
    def move(self):
         #code to get our snake to automatically move foward
        for seg_num in range(len(self.segment)-1, 0,-1): ## looping backwards like 3,2,1   len(segment)-1#because it counts from 1,2,3 and we know indexes start from 0 
            new_x=self.segment[seg_num-1].xcor() #this is the second last postion get the x coordinates
            new_y=self.segment[seg_num-1].ycor() #get the y coodinates
            self.segment[seg_num].goto(new_x,new_y) #starts a postion 2
        self.head.forward(MOVE_DISTANCE)
        
        
    def add_segment(self,position):#creates the startinf snake the one square in the middle
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segment.append(new_segment)#creates the starting snake
            
            
    def extend(self):
        self.add_segment(self.segment[-1].position())#get hold of the last segment of the list
                    
        
    def up(self):
        if self.head.heading()!= DOWN: #prevent the snake from going backwards
            self.head.setheading(UP)
            
            
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
            
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)
            
        
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    
     #resets the snake for the game       
    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)#tells the segment to go off the screen
        self.segment.clear()
        self.create_snake()
        self.head=self.segment[0]
           