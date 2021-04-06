#This program will display a playable maze with a moving part of the maze.
from tkinter import *

#Set the height and width of the window

width = 800
height = 800

class Maze:
    def __init__(self):
        window = Tk() #Creates the window

        window.title('Move the ball with the arrow keys') #Sets the title

        #Set the canvas

        self.canvas = Canvas(window,bg = "Green", width = width, height = height)
        self.canvas.pack()

        x = 20
        dx = 5
        
        #Create maze working from the outside and going in
        self.canvas.create_rectangle(0,0,10,800,fill = "Black")
        self.canvas.create_rectangle(10,790,800,800,fill = "Black")
        self.canvas.create_rectangle(790,0,800,780,fill = "Black")
        self.canvas.create_rectangle(20,0,790,10,fill = "Black")
        self.canvas.create_rectangle(20,10,30,150,fill = "Black")
        self.canvas.create_rectangle(20,160,30,290,fill = "Black")
        self.canvas.create_rectangle(10,300,30,310,fill = "Black")
        self.canvas.create_rectangle(10,320,30,330,fill = "Black")
        self.canvas.create_rectangle(10,360,50,370,fill = "Black")
        self.canvas.create_rectangle(40,370,50,780,fill = "Black")
        self.canvas.create_rectangle(20,770,40,780,fill = "Black")
        self.canvas.create_rectangle(20,380,30,770,fill = "Black")
        self.canvas.create_rectangle(60,360,70,790,fill = "Black") #Reference
        self.canvas.create_rectangle(40,290,50,340,fill = "Black")
        self.canvas.create_rectangle(20,340,381,350,fill = "Black")  #Leave a copy of moving rectangle
        self.canvas.create_rectangle(20,340,380,350,fill = "Black", tags = "Rectangle") #Move right
        self.canvas.create_rectangle(380,300,390,780,fill = "Black")  #Start of Spiral
        self.canvas.create_rectangle(20,280,100,290,fill = "Black")
        self.canvas.create_rectangle(80,770,380,780,fill = "Black") 
        self.canvas.create_rectangle(80,360,90,780, fill = "Black")
        self.canvas.create_rectangle(80,360,370,370,fill = "Black")
        self.canvas.create_rectangle(360,370,370,760,fill = "Black")
        self.canvas.create_rectangle(100,750,360,760,fill = "Black")
        self.canvas.create_rectangle(100,380,110,750,fill = "Black")
        self.canvas.create_rectangle(110,380,350,390,fill = "Black")
        self.canvas.create_rectangle(340,380,350,740,fill = "Black")
        self.canvas.create_rectangle(120,730,340,740,fill = "Black")
        self.canvas.create_rectangle(120,400,130,730,fill = "Black")
        self.canvas.create_rectangle(130,400,330,410,fill = "Black")
        self.canvas.create_rectangle(320,410,330,710,fill = "Black")
        self.canvas.create_rectangle(140,710,330,720,fill = "Black")
        self.canvas.create_rectangle(140,420,150,710,fill = "Black")
        self.canvas.create_rectangle(150,420,310,430,fill = "Black")
        self.canvas.create_rectangle(300,430,310,700,fill = "Black")
        self.canvas.create_rectangle(160,690,300,700,fill = "Black")
        self.canvas.create_rectangle(160,440,170,690,fill = "Black")
        self.canvas.create_rectangle(170,440,290,450,fill = "Black")
        self.canvas.create_rectangle(280,440,290,680,fill = "Black")
        self.canvas.create_rectangle(180,670,280,680,fill = "Black")
        self.canvas.create_rectangle(180,460,190,680,fill = "Black")
        self.canvas.create_rectangle(190,460,270,470,fill = "Black")
        self.canvas.create_rectangle(260,470,270,660,fill = "Black")
        self.canvas.create_rectangle(200,650,260,660,fill = "Black")
        self.canvas.create_rectangle(200,480,210,650,fill = "Black")
        self.canvas.create_rectangle(210,480,250,490,fill = "Black")
        self.canvas.create_rectangle(240,490,250,640,fill = "Black")
        self.canvas.create_rectangle(220,630,240,640,fill = "Black")
        self.canvas.create_rectangle(220,500,230,630,fill = "Black")   
        self.canvas.create_rectangle(220,500,230,631,fill = "Black")
        self.canvas.create_rectangle(400,20,410,790,fill = "Black")    #Center Divide
        self.canvas.create_rectangle(420,770,780,780,fill = "Black")   #Bottom right rectangle by starting position
        self.canvas.create_rectangle(770,710,780,780,fill = "Black")      #First upward rectangle by start
        self.canvas.create_rectangle(600,760,610,770,fill = "Black")
        self.canvas.create_rectangle(410,750,610,760,fill = "Black")
        self.canvas.create_rectangle(760,690,790,700,fill = "Black")
        self.canvas.create_rectangle(750,690,760,760,fill = "Black")
        self.canvas.create_rectangle(620,750,750,760,fill = "Black")
        self.canvas.create_rectangle(620,730,750,740,fill = "Black")
        self.canvas.create_rectangle(420,670,610,680,fill = "Black")
        self.canvas.create_rectangle(420,680,430,750,fill = "Black")
        self.canvas.create_rectangle(440,690,600,700,fill = "Black")
        self.canvas.create_rectangle(440,710,750,720,fill = "Black")
        self.canvas.create_rectangle(600,680,610,700,fill = "Black")
        self.canvas.create_rectangle(440,730,610,740,fill = "Black")
        self.canvas.create_rectangle(525,740,535,750,fill = "Black")
        self.canvas.create_rectangle(620,660,630,710,fill = "Black")
        self.canvas.create_rectangle(420,650,630,660,fill = "Black")
        self.canvas.create_rectangle(410,630,640,640,fill = "Black")
        self.canvas.create_rectangle(640,630,650,700,fill = "Black")
        self.canvas.create_rectangle(650,690,740,700,fill = "Black")
        self.canvas.create_rectangle(660,670,790,680,fill = "Black")
        self.canvas.create_rectangle(650,650,780,660,fill = "Black")
        self.canvas.create_rectangle(660,630,790,640,fill = "Black")
        self.canvas.create_rectangle(420,610,780,620,fill = "Black")
        self.canvas.create_rectangle(420,500,430,610,fill = "Black")
        self.canvas.create_rectangle(410,480,440,490,fill = "Black")
        self.canvas.create_rectangle(440,480,450,600,fill = "Black")   #Start of staircase #1
        self.canvas.create_rectangle(450,480,460,590,fill = "Black")
        self.canvas.create_rectangle(460,480,470,580,fill = "Black")
        self.canvas.create_rectangle(470,480,480,570,fill = "Black")
        self.canvas.create_rectangle(480,480,490,560,fill = "Black")
        self.canvas.create_rectangle(490,480,500,550,fill = "Black")
        self.canvas.create_rectangle(500,480,510,540,fill = "Black")
        self.canvas.create_rectangle(510,480,520,530,fill = "Black")
        self.canvas.create_rectangle(520,480,530,520,fill = "Black")
        self.canvas.create_rectangle(530,480,540,510,fill = "Black")
        self.canvas.create_rectangle(540,480,550,500,fill = "Black")
        self.canvas.create_rectangle(550,480,560,490,fill = "Black")   #End of staircase #1
        self.canvas.create_rectangle(770,500,780,610,fill = "Black")
        self.canvas.create_rectangle(760,480,790,490,fill = "Black")
        self.canvas.create_rectangle(750,480,760,600,fill = "Black")    #Start of staircase #2
        self.canvas.create_rectangle(740,490,750,600,fill = "Black")
        self.canvas.create_rectangle(730,500,740,600,fill = "Black")
        self.canvas.create_rectangle(720,510,730,600,fill = "Black")
        self.canvas.create_rectangle(710,520,720,600,fill = "Black")
        self.canvas.create_rectangle(700,530,710,600,fill = "Black")
        self.canvas.create_rectangle(690,540,700,600,fill = "Black")
        self.canvas.create_rectangle(680,550,690,600,fill = "Black")
        self.canvas.create_rectangle(670,560,680,600,fill = "Black")
        self.canvas.create_rectangle(660,570,670,600,fill = "Black")
        self.canvas.create_rectangle(650,580,660,600,fill = "Black")
        self.canvas.create_rectangle(640,590,650,600,fill = "Black")   #End of staircase #2
        self.canvas.create_rectangle(560,480,570,600,fill = "Black")   #Inner Maze
        self.canvas.create_rectangle(630,480,640,600,fill = "Black")
        self.canvas.create_rectangle(580,590,630,600,fill = "Black")
        self.canvas.create_rectangle(580,570,620,580,fill = "Black")
        self.canvas.create_rectangle(610,560,620,570,fill = "Black")
        self.canvas.create_rectangle(570,550,620,560,fill = "Black")
        self.canvas.create_rectangle(580,530,630,540,fill = "Black")
        self.canvas.create_rectangle(580,510,590,520,fill = "Black")
        self.canvas.create_rectangle(610,510,620,520,fill = "Black")
        self.canvas.create_rectangle(580,490,620,500,fill = "Black")   #End of Inner Maze
        self.canvas.create_rectangle(420,460,560,470,fill = "Black")   #Break 1
        self.canvas.create_rectangle(570,460,680,470,fill = "Black")   #Break 2
        self.canvas.create_rectangle(690,460,780,470,fill = "Black")   #Break 3
        self.canvas.create_rectangle(770,370,780,460,fill = "Black")
        self.canvas.create_rectangle(670,360,790,370,fill = "Black")   
        self.canvas.create_rectangle(670,440,680,460,fill = "Black")
        self.canvas.create_rectangle(680,440,760,450,fill = "Black")
        self.canvas.create_rectangle(750,380,760,440,fill = "Black")
        self.canvas.create_rectangle(730,360,740,430,fill = "Black")
        self.canvas.create_rectangle(710,380,720,440,fill = "Black")
        self.canvas.create_rectangle(670,370,680,430,fill = "Black")
        self.canvas.create_rectangle(650,340,660,430,fill = "Black")   ##
        self.canvas.create_rectangle(650,440,660,460,fill = "Black")   ##
        self.canvas.create_rectangle(660,340,790,350,fill = "Black")
        self.canvas.create_rectangle(680,380,700,390,fill = "Black")
        self.canvas.create_rectangle(690,400,710,410,fill = "Black")
        self.canvas.create_rectangle(680,420,700,430,fill = "Black")
        self.canvas.create_rectangle(420,360,430,460,fill = "Black")
        self.canvas.create_rectangle(410,340,440,350,fill = "Black")  
        self.canvas.create_rectangle(440,340,450,450,fill = "Black")
        self.canvas.create_rectangle(450,440,640,450,fill = "Black")
        self.canvas.create_rectangle(460,420,650,430,fill = "Black")
        self.canvas.create_rectangle(460,340,470,420,fill = "Black")
        self.canvas.create_rectangle(410,320,530,330,fill = "Black")   #Top Right Rectangles
        self.canvas.create_rectangle(540,320,690,330,fill = "Black")
        self.canvas.create_rectangle(590,310,600,320,fill = "Black")
        self.canvas.create_rectangle(700,320,790,330,fill = "Black")
        self.canvas.create_rectangle(410,300,500,310,fill = "Black")
        self.canvas.create_rectangle(411,300,500,310,fill = "Black")
        self.canvas.create_rectangle(510,300,690,310,fill = "Black")
        self.canvas.create_rectangle(580,290,590,300,fill = "Black")
        self.canvas.create_rectangle(700,300,790,310,fill = "Black")
        self.canvas.create_rectangle(410,280,550,290,fill = "Black")
        self.canvas.create_rectangle(540,270,550,280,fill = "Black")
        self.canvas.create_rectangle(610,280,790,290,fill = "Black")
        self.canvas.create_rectangle(560,280,600,290,fill = "Black")
        self.canvas.create_rectangle(410,260,470,270,fill = "Black")
        self.canvas.create_rectangle(480,260,590,270,fill = "Black")
        self.canvas.create_rectangle(520,250,530,260,fill = "Black")
        self.canvas.create_rectangle(600,260,790,270,fill = "Black")
        self.canvas.create_rectangle(420,240,540,250,fill = "Black")
        self.canvas.create_rectangle(550,240,640,250,fill = "Black")
        self.canvas.create_rectangle(570,230,580,240,fill = "Black")
        self.canvas.create_rectangle(650,240,780,250,fill = "Black")
        self.canvas.create_rectangle(410,220,440,230,fill = "Black")
        self.canvas.create_rectangle(450,220,670,230,fill = "Black")
        self.canvas.create_rectangle(540,210,550,220,fill = "Black")
        self.canvas.create_rectangle(680,220,790,230,fill = "Black")
        self.canvas.create_rectangle(410,200,420,210,fill = "Black")
        self.canvas.create_rectangle(430,200,530,210,fill = "Black")
        self.canvas.create_rectangle(540,200,790,210,fill = "Black")
        self.canvas.create_rectangle(610,190,620,200,fill = "Black")
        self.canvas.create_rectangle(410,180,470,190,fill = "Black")
        self.canvas.create_rectangle(480,180,600,190,fill = "Black")
        self.canvas.create_rectangle(550,170,560,180,fill = "Black")
        self.canvas.create_rectangle(610,180,780,190,fill = "Black")
        self.canvas.create_rectangle(410,160,540,170,fill = "Black")
        self.canvas.create_rectangle(550,160,760,170,fill = "Black")
        self.canvas.create_rectangle(590,150,600,160,fill = "Black")
        self.canvas.create_rectangle(770,160,790,170,fill = "Black")
        self.canvas.create_rectangle(410,140,440,150,fill = "Black")
        self.canvas.create_rectangle(450,140,660,150,fill = "Black")
        self.canvas.create_rectangle(650,130,660,140,fill = "Black")
        self.canvas.create_rectangle(670,140,790,150,fill = "Black")
        self.canvas.create_rectangle(420,120,460,130,fill = "Black")
        self.canvas.create_rectangle(470,120,540,130,fill = "Black")
        self.canvas.create_rectangle(520,110,530,120,fill = "Black")
        self.canvas.create_rectangle(550,120,790,130,fill = "Black")
        self.canvas.create_rectangle(420,100,440,110,fill = "Black")
        self.canvas.create_rectangle(450,100,670,110,fill = "Black")
        self.canvas.create_rectangle(660,90,670,100,fill = "Black")
        self.canvas.create_rectangle(680,100,780,110,fill = "Black")
        self.canvas.create_rectangle(410,80,650,90,fill = "Black")
        self.canvas.create_rectangle(660,80,750,90,fill = "Black")
        self.canvas.create_rectangle(500,70,510,80,fill = "Black")
        self.canvas.create_rectangle(760,80,790,90,fill = "Black")
        self.canvas.create_rectangle(410,60,470,70,fill = "Black")
        self.canvas.create_rectangle(480,60,560,70,fill = "Black")
        self.canvas.create_rectangle(570,60,780,70,fill = "Black")
        self.canvas.create_rectangle(680,50,690,60,fill = "Black")
        self.canvas.create_rectangle(420,40,490,50,fill = "Black")
        self.canvas.create_rectangle(500,40,690,50,fill = "Black")
        self.canvas.create_rectangle(560,30,570,40,fill = "Black")
        self.canvas.create_rectangle(700,40,790,50,fill = "Black")
        self.canvas.create_rectangle(410,20,780,30,fill = "Black")
        self.canvas.create_rectangle(40,20,400,30,fill = "Black")   #Start of Top Left Rectangles
        self.canvas.create_rectangle(30,40,200,50,fill = "Black")
        self.canvas.create_rectangle(210,40,300,50,fill = "Black")
        self.canvas.create_rectangle(240,30,250,40,fill = "Black")
        self.canvas.create_rectangle(310,40,400,50,fill = "Black")
        self.canvas.create_rectangle(30,60,170,70,fill = "Black")
        self.canvas.create_rectangle(180,60,240,70,fill = "Black")
        self.canvas.create_rectangle(190,50,200,60,fill = "Black")
        self.canvas.create_rectangle(250,60,400,70,fill = "Black")
        self.canvas.create_rectangle(40,80,110,90,fill = "Black")
        self.canvas.create_rectangle(120,80,180,90,fill = "Black")
        self.canvas.create_rectangle(150,70,160,80,fill = "Black")
        self.canvas.create_rectangle(190,80,400,90,fill = "Black")
        self.canvas.create_rectangle(30,100,130,110,fill = "Black")
        self.canvas.create_rectangle(140,100,290,110,fill = "Black")
        self.canvas.create_rectangle(270,90,280,100,fill = "Black")
        self.canvas.create_rectangle(300,100,400,110,fill = "Black")
        self.canvas.create_rectangle(40,120,140,130,fill = "Black")
        self.canvas.create_rectangle(150,120,250,130,fill = "Black")
        self.canvas.create_rectangle(260,120,390,130,fill = "Black")
        self.canvas.create_rectangle(190,110,200,120,fill = "Black")
        self.canvas.create_rectangle(30,140,170,150,fill = "Black")
        self.canvas.create_rectangle(180,140,260,150,fill = "Black")
        self.canvas.create_rectangle(270,140,400,150,fill = "Black")
        self.canvas.create_rectangle(70,130,80,140,fill = "Black")
        self.canvas.create_rectangle(40,160,100,170,fill = "Black")
        self.canvas.create_rectangle(110,160,280,170,fill = "Black")
        self.canvas.create_rectangle(290,160,400,170,fill = "Black")
        self.canvas.create_rectangle(60,150,70,160,fill = "Black")
        self.canvas.create_rectangle(230,150,240,160,fill = "Black")
        self.canvas.create_rectangle(30,180,130,190,fill = "Black")
        self.canvas.create_rectangle(140,180,310,190,fill = "Black")
        self.canvas.create_rectangle(200,170,210,180,fill = "Black")
        self.canvas.create_rectangle(320,180,400,190,fill = "Black")
        self.canvas.create_rectangle(40,200,170,210,fill = "Black")
        self.canvas.create_rectangle(100,190,110,200,fill = "Black")
        self.canvas.create_rectangle(180,200,260,210,fill = "Black")
        self.canvas.create_rectangle(250,190,260,200,fill = "Black")
        self.canvas.create_rectangle(270,200,390,210,fill = "Black")
        self.canvas.create_rectangle(30,220,150,230,fill = "Black")
        self.canvas.create_rectangle(160,220,230,230,fill = "Black")
        self.canvas.create_rectangle(240,220,400,230,fill = "Black")
        self.canvas.create_rectangle(250,210,260,220,fill = "Black")
        self.canvas.create_rectangle(30,240,70,250,fill = "Black")
        self.canvas.create_rectangle(80,240,290,250,fill = "Black")
        self.canvas.create_rectangle(300,240,400,250,fill = "Black")
        self.canvas.create_rectangle(170,230,180,240,fill = "Black")
        self.canvas.create_rectangle(40,260,130,270,fill = "Black")
        self.canvas.create_rectangle(140,260,320,270,fill = "Black")
        self.canvas.create_rectangle(200,250,210,260,fill = "Black")
        self.canvas.create_rectangle(330,260,400,270,fill = "Black")
        self.canvas.create_rectangle(110,280,120,300,fill = "Black")
        self.canvas.create_rectangle(60,300,120,310,fill = "Black")
        self.canvas.create_rectangle(120,280,400,290,fill = "Black")
        self.canvas.create_rectangle(60,310,70,330,fill = "Black")
        self.canvas.create_rectangle(70,320,370,330,fill = "Black")
        self.canvas.create_rectangle(130,300,380,310,fill = "Black")
        #Ball
        self.canvas.create_oval(791,781,799,789,fill = "Red",tags = "Ball")

        #Bind the arrow keys to move
        self.canvas.bind("<Up>",self.Up)
        self.canvas.bind("<Down>",self.Down)
        self.canvas.bind("<Left>",self.Left)
        self.canvas.bind("<Right>",self.Right)
        self.canvas.focus_set()
       


        while True:
            self.canvas.move("Rectangle",x,0)

            self.canvas.after(50)
            self.canvas.update()
            if x < 400:
                x += dx
            else:
                x = 0
            self.canvas.delete("Rectangle")
            self.canvas.create_rectangle(20,340,380,350,fill = "Black", tags = "Rectangle")
            self.canvas.move("Rectangle",x,0)
        window.mainloop()
         

    def Left(self,event):
        self.canvas.move("Ball",-10,0)

    def Right(self,event):
        self.canvas.move("Ball",10,0)

    def Up(self,event):
        self.canvas.move("Ball",0,-10)

    def Down(self,event):
        self.canvas.move("Ball",0,10)
Maze()

#Yes I did check to see if it is possible to make it from start to finish and it is.
