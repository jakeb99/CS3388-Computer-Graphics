import operator
from PIL import Image

class graphicsWindow:
    """ This class implements Bresenham's integer line algorithm.

    Course: CS 3388B
    Title: Assignment 1
    Author: jbuntin4
    Module: graphicsWindow.py
    Date created: Jan 14th, 2021

    Specifically, drawLine(), drawLineGradual(), and drawLineSteep() implement the
    algorithm to complete this assignment, all other code provided by instructor.

    """
    def __init__(self,width=640,height=480):
        self.__mode = 'RGB'
        self.__width = width
        self.__height = height
        self.__canvas = Image.new(self.__mode,(self.__width,self.__height))
        self.__image = self.__canvas.load()

    def drawPoint(self,point,color):
        if 0 <= point[0] < self.__width and 0 <= point[1] < self.__height:
            self.__image[point[0],point[1]] = color

    def drawLine(self,point1,point2,color):
        """ Draws a line using Bresenham's integer line algorithm

        This method calls drawLineGradual() or drawLineSteep() which are helper methods that
        actually implement the integer line algorithm for a line with a gentle or steep slope.

        Parameters
        ----------
        point1 : matrix
            A column vector storing the x and y coordinates of the start of the line.
        point2 : matrix
            A column vector storing the x and y coordinates of the end of the line.
        color : tuple
            A tuple denoted (r, g, b) that stores the colour of the pixels to be
            drawn to the window.
        """
        # Store the values of the matrices storing point1 and point2
        x1 = int(point1.get(0,0))
        y1 = int(point1.get(1,0))
        x2 = int(point2.get(0,0))
        y2 = int(point2.get(1,0))

        if abs(y2 - y1) < abs(x2 - x1):     # case for drawing a line with a gradual slope (i.e., slope between 0 and 1 or 0 and -1)
            if x1 < x2:
                self.drawLineGradual(x1, y1, x2, y2, color)
            else:   # swap the points to draw the line in the other direction
                self.drawLineGradual(x2, y2, x1, y1, color)
        else:                               # case for drawing a line with a steep slope (i.e., greater than 1)
            if y1 < y2:
                self.drawLineSteep(x1, y1, x2, y2, color)
            else:   # swap the points to draw the line in the other direction
                self.drawLineSteep(x2, y2, x1, y1, color)


    def drawLineGradual(self, x1, y1, x2, y2, color):
        """" Draws lines with gradual slopes
        Parameters
        ----------
        x1, y1, x2, y2 : int
            These points (x1, y1) and (x2, y2) define the line the algorithm will draw
        color : tuple
            A tuple denoted (r, g, b) that stores the colour of the pixels to be
            drawn to the window.
        """
        dx = x2 - x1        # change in x
        dy = y2 - y1        # change in y
        z = 1

        if dy < 0:          # check if y should increase or decrease
            dy *= -1
            z = -1

        self.drawPoint([x1,y1],color)   # draw the initial point

        pi = 0      # pixel/point
        for i in range(x1,x2):      # loop to calculate the coordinate of next pixel
            if i == x1:
                pi = 2 * dy - dx    # on first iteration, pi = p1
            else:
                if pi < 0:
                    pi += 2 * dy
                else:
                    pi += 2 * dy - 2 * dx
                    y1 += z         # z is either 1 or -1 depending if dy < 0
                x1 += 1
                self.drawPoint([x1,y1],color)       # draw the point

    def drawLineSteep(self, x1, y1, x2, y2, color):
        """" Draws lines with steep slopes

        This algorithm is basically the same as the above but we swap x and y, dx and dy to
        inverse th slope and draw along the x-axis instead of the y-axis.

        Parameters
        ----------
        x1, y1, x2, y2 : int
            These points (x1, y1) and (x2, y2) define the line the algorithm will draw
        color : tuple
            A tuple denoted (r, g, b) that stores the colour of the pixels to be
            drawn to the window.
        """
        dx = x2 - x1        # change in x
        dy = y2 - y1        # change in y
        z = 1

        if dx < 0:          # determine if x should increase or decrease
            dx *= -1
            z = -1

        self.drawPoint([x1,y1],color)   # draw the initial point

        pi = 0      # pixel/point
        for i in range(y1, y2):     # loop to calculate next coord for the pixel
            if i == y1:
                pi = 2 * dx - dy    # on first iteration, pi = p1
            else:
                if pi < 0:
                    pi += 2 * dx
                else:
                    pi += 2 * dx - 2 * dy
                    x1 += z                 # z is either 1 or -1 depending if dx < 0
                y1 += 1
                self.drawPoint([x1,y1],color)   # draw the point

    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height
