import numpy as np
import cv2

#Map Creation using Half Plane Method & OpenCV
class visualization():
    def __init__(self):
        #Empty Lists to store the equations of the lines
        self.rect1_n_eq = []
        self.rect2_n_eq = []
        self.hexa_n_eq = []
        self.trig_n_eq = []
        
        self.rect1_b_eq = []
        self.rect2_b_eq = []
        self.hexa_b_eq = []
        self.trig_b_eq = []
        self.walls_eq = []

    #Function to calculate the equation of a line given two points
    def line_eq(self, pt1, pt2):
        a = pt2[1] - pt1[1] #a = y2 - y1
        b = pt1[0] - pt2[0] #b = x1 - x2
        c = a*(pt1[0]) + b*(pt1[1]) #-c = ax1 + by1
        return [a, b, -c] #return the equation of the line

    #Function to cal line equation of all the obstacles & check if a node is inside the obstacle space
    def map_half_plane(self): 
        #Normal Obstacle Space: (points taken in clock-wise order)
        rect1_n = [(100,0), (150,0), (150,100), (100,100), (100,0)]
        rect2_n = [(100,150), (150,150), (150,250), (100,250), (100,150)]
        hexagon_n = [(300,50), (360, 87), (360,163), (300,200), (240,163), (240,87), (300,50)]
        trig_n = [(460,25), (510,125), (460,225), (460,25)]

        #Bloated Obstacle Space: (points taken in clock-wise order)
        rect1_b = [(95,0), (155,0), (155,105), (95,105), (95,0)] #Rectangle obstacle
        rect2_b = [(95,145), (155,145), (155,250), (95,250), (95,145)] #Rectangle obstacle
        hexagon_b = [(300,45), (365, 85), (365,165), (300,205), (235,165), (235,85), (300,45)] #Hexagon obstacle
        trig_b = [(455,5), (515,125), (455,245), (455,5)] #Triangle obstacle
        walls = [(5, 5), (595,5), (595,245), (5,245), (5,5)] #Boundary of the map

        self.image = np.zeros((600, 250, 3), np.uint8) #create a new image with a black background

        for i in range(len(rect1_n)-1): #Find the equation of all the lines of rect obstacles
            self.rect1_n_eq.append(self.line_eq(rect1_n[i], rect1_n[i+1])) #Normal rect obstacle eqn
            self.rect1_b_eq.append(self.line_eq(rect1_b[i], rect1_b[i+1])) #Bloated rect obstacle eqn
            self.rect2_n_eq.append(self.line_eq(rect2_n[i], rect2_n[i+1])) #Normal rect obstacle eqn
            self.rect2_b_eq.append(self.line_eq(rect2_b[i], rect2_b[i+1])) #Bloated rect obstacle eqn
            self.walls_eq.append(self.line_eq(walls[i], walls[i+1])) #Bloated wall eqn

        for i in range(len(hexagon_n)-1): #Find the equation of all the lines of hexagon obstacles
            self.hexa_n_eq.append(self.line_eq(hexagon_n[i], hexagon_n[i+1])) #Normal hexagon obstacle eqn
            self.hexa_b_eq.append(self.line_eq(hexagon_b[i], hexagon_b[i+1])) #Bloated hexagon obstacle eqn

        for i in range(len(trig_n)-1): #Find the equation of all the lines of triangle obstacles
            self.trig_n_eq.append(self.line_eq(trig_n[i], trig_n[i+1])) #Normal triangle obstacle eqn
            self.trig_b_eq.append(self.line_eq(trig_b[i], trig_b[i+1])) #Bloated triangle obstacle eqn

        def check_poly(poly, x, y): #Function to check if a node is inside any polygon obstacle space
            count = 0
            for i in range(len(poly)): 
                if poly[i][0] * x + poly[i][1] * y + poly[i][2] <= 0: #Check if the node is on the left side of the line
                    count+=1 #If yes, increment the count
            
            if count == len(poly): #If the count is equal to the number of lines, the node is inside the polygon
                return True
            
        for i in range(0, 600): #Loop through all the nodes in the map
            for j in range(0, 250): 
                if (check_poly(self.rect1_b_eq, i, j) == True): #Check if the node is inside the bloated rect 1 obstacle space
                    if (check_poly(self.rect1_n_eq, i, j) == True): #Check if the node is inside the normal rect 1 obstacle space
                        self.image[i][j] = [255, 255, 255]
                    else:
                        self.image[i][j] = [255, 191, 0]
                
                elif (check_poly(self.rect2_b_eq, i, j) == True): #Check if the node is inside the bloated rect 2 obstacle space
                    if (check_poly(self.rect2_n_eq, i, j) == True): #Check if the node is inside the normal rect 2 obstacle space
                        self.image[i][j] = [255, 255, 255]
                    else:
                        self.image[i][j] = [255, 191, 0]

                elif (check_poly(self.hexa_b_eq, i, j) == True): #Check if the node is inside the bloated hexagon obstacle space
                    if (check_poly(self.hexa_n_eq, i, j) == True): #Check if the node is inside the normal hexagon obstacle space
                        self.image[i][j] = [255, 255, 255]
                    else:
                        self.image[i][j] = [255, 191, 0]

                elif (check_poly(self.trig_b_eq, i, j) == True): #Check if the node is inside the bloated triangle obstacle space
                    if (check_poly(self.trig_n_eq, i, j) == True): #Check if the node is inside the normal triangle obstacle space
                        self.image[i][j] = [255, 255, 255]
                    else:
                        self.image[i][j] = [255, 191, 0]

                elif (not((i >=5 and i <= 595) and (j >= 5 and j <= 245))): #Check if the node is not inside the bloated wall space
                    self.image[i][j] = [255, 191, 0]
 
        return self.image #Return the image with the map

    def highLight_node(self, node, color): #Function to highlight a node in the map
        self.image[node[0],node[1]] = color #Change the color of the node to the specified color

    def highLight_position(self, node, color): #Function to highlight the point robot in the map
        plot = self.image.copy()
        cv2.circle(plot, (node[1],node[0]), 5, color, 3) #Draw a circle at the specified node
        return plot