import os
import sys
import pygame

class CapGesture():
    mode = False
    position = 0.0
    pygame.init()
    on = False
    capture = False
    capFileName = 0
    def __init__(self):
      if len(sys.argv) > 1:
          if sys.argv[1] == "--capture":
              self.mode = True
    def writeOut(self):
        print("doot")
        #pygame.init()

        print("Pressing select on the psmove will exit")
        if self.capture:
            joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
            for i in range(0, len(joysticks)):
                joysticks[i].init()
            
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                   for c in range(0, joysticks[i].get_numbuttons()):
                        if joysticks[i].get_button(c) == 1:
                            print("Button number ", c, "down")
                            down = True
                   #pygame.joystick.quit()
                   
                if event.type == pygame.JOYBUTTONUP:
                   up = True
                   self.on = False
                   self.capFile.close()
                   self.capture = False
                   print("up")
                   
            for i in range(0, len(joysticks)):
                pos = 0
                print(joysticks[i].get_axis(1))
                print(joysticks[i].get_axis(2))
                print(joysticks[i].get_axis(3))
                print(joysticks[i].get_axis(4))
                if joysticks[i].get_axis(1):
                        self.position += joysticks[i].get_axis(1)
                        self.capFile.write(""+str(joysticks[i].get_axis(1)))
                        self.capFile.write(","+str(joysticks[i].get_axis(2)))
                        self.capFile.write(","+str(joysticks[i].get_axis(3)))
                        self.capFile.write(","+str(joysticks[i].get_axis(4)))
                        self.capFile.write("\n")
                    
                        
                if joysticks[i].get_axis(2):
                        
                        self.capFile.write(""+str(joysticks[i].get_axis(1)))
                        self.capFile.write(","+str(joysticks[i].get_axis(2)))
                        self.capFile.write(","+str(joysticks[i].get_axis(3)))
                        self.capFile.write(","+str(joysticks[i].get_axis(4)))
                        self.capFile.write("\n")
                        self.position += joysticks[i].get_axis(2)
                if joysticks[i].get_axis(3):
                        
                        self.capFile.write(""+str(joysticks[i].get_axis(1)))
                        self.capFile.write(","+str(joysticks[i].get_axis(2)))
                        self.capFile.write(","+str(joysticks[i].get_axis(3)))
                        self.capFile.write(","+str(joysticks[i].get_axis(4)))
                        self.capFile.write("\n")
                        self.position += joysticks[i].get_axis(3)
                if joysticks[i].get_axis(4):
                        
                        self.capFile.write(""+str(joysticks[i].get_axis(1)))
                        self.capFile.write(","+str(joysticks[i].get_axis(2)))
                        self.capFile.write(","+str(joysticks[i].get_axis(3)))
                        self.capFile.write(","+str(joysticks[i].get_axis(4)))
                        self.capFile.write("\n")
                        self.position += joysticks[i].get_axis(4)
                
                #if joysticks[i].get_name() == "Navigation Controller":
                #    print(joysticks[i].get_name())
                #else:
                #    print(joysticks[i].get_name())
                #These are the axes we wish to capture
                #0 is the trigger
                #1-4 are the axes
                for x in range(0, joysticks[i].get_numaxes()):
                    axes = joysticks[i].get_numaxes() 
                joysticks[i].get_numbuttons()
                
                for c in range(0, joysticks[i].get_numbuttons()):
                    if joysticks[i].get_button(c) == 1 and c == 14:
                        print("POSITION ::::",self.position,"::::")
                    if joysticks[i].get_button(c) == 1 and c == 0:
                        sys.exit(1)
 
    def scribe(self):
        print("doot")
        #pygame.init()

        print("Pressing select on the psmove will exit")
        if True:
            joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
            for i in range(0, len(joysticks)):
                joysticks[i].init()
            #self.capture = False
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                   for c in range(0, joysticks[i].get_numbuttons()):
                        if joysticks[i].get_button(c) == 1:
                            print("Button number ", c, "down")
                        if joysticks[i].get_button(20) == 1:
                            print("Capturing axes!")
                            self.capture = True
                            own = True
                   #pygame.joystick.quit()
                   return
                if event.type == pygame.JOYBUTTONUP:
                   up = True
                   print("up")
                   return
            for i in range(0, len(joysticks)):
                pos = 0
                print(joysticks[i].get_axis(1))
                print(joysticks[i].get_axis(2))
                print(joysticks[i].get_axis(3))
                print(joysticks[i].get_axis(4))
                if joysticks[i].get_axis(1):
                    if joysticks[i].get_axis(1) > 0:
                        self.position += joysticks[i].get_axis(1)
                        print("move 1 :",joysticks[i].get_axis(1))
                        
                    else:
                        self.position += joysticks[i].get_axis(1)
                        print("move 1 :",joysticks[i].get_axis(1))
                        
                if joysticks[i].get_axis(2):
                    if joysticks[i].get_axis(2) > 0:
                        
                        print("move 2 :",joysticks[i].get_axis(2))
                        self.position += joysticks[i].get_axis(2)
                    else:
                        
                        print("move 2 :",joysticks[i].get_axis(2))
                        self.position += joysticks[i].get_axis(2)
                if joysticks[i].get_axis(3):
                    if joysticks[i].get_axis(3) > 0:
                        
                        print("move 3 :",joysticks[i].get_axis(3))
                        self.position += joysticks[i].get_axis(3)
                    else:
                        
                        print("move 3 :",joysticks[i].get_axis(3))
                        self.position += joysticks[i].get_axis(3)
                if joysticks[i].get_axis(4):
                    if joysticks[i].get_axis(4) > 0:
                        
                        print("move 4 :",joysticks[i].get_axis(4))
                        self.position += joysticks[i].get_axis(4)
                    else:
                        print("move 4 :",joysticks[i].get_axis(4))
                        self.position += joysticks[i].get_axis(4)
                #if joysticks[i].get_name() == "Navigation Controller":
                #    print(joysticks[i].get_name())
                #else:
                #    print(joysticks[i].get_name())
                #These are the axes we wish to capture
                #0 is the trigger
                #1-4 are the axes
                for x in range(0, joysticks[i].get_numaxes()):
                    axes = joysticks[i].get_numaxes() 
                joysticks[i].get_numbuttons()
                
                for c in range(0, joysticks[i].get_numbuttons()):
                    if joysticks[i].get_button(c) == 1 and c == 14:
                        print("POSITION ::::",self.position,"::::")
                    if joysticks[i].get_button(c) == 1 and c == 0:
                        self.outfile.close()
                        sys.exit(1)
                if self.capture and not self.on:
                    self.capFile = open('data/gestures/'+str(self.capFileName)+'.ges', 'a')
                    self.capFileName += 1
                    self.on = True
        #pygame.joystick.quit()

thing = CapGesture()

thing.scribe()