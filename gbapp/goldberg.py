import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
import time

# This project has been implemented and tested on Python 3.8.0
# by Taha Yasin for the course Ceng445 in semester 20191

class User:
    """ User class creates, modifies and observing Board & Shape classes. """
    user_count = 0
    user_name = "Unknown"
    def __init__(self, user_name="Player"):
        User.user_count += 1
        self.user_name = user_name
        print("A user has been created with the name", self.user_name, "and current user count is:", User.user_count)
    
    def get(self):
        return self.user_name
    
    def rename(self, newname="Player++"):
        oldname = self.user_name
        self.user_name = newname
        print("Player  \'", oldname, "\' has been renamed to  \'", self.user_name, "\'")

class Board:
    board_count = 0
    board_name = "Unknown"
    user_list = []
    board_list = []
    def __init__(self, x=1280, y= 720, board_name ="Board#0"):
        Board.board_count += 1
        self.board_name = board_name
        self.board_space = pymunk.Space()
        self.board_space.gravity = 0, -100
        Board.board_list.append(self)
        print("A board has been created with the name", self.board_name, "and current board count is:", self.board_count)
    
    def addShape(self, shape, x, y):
        shape.setPosition(x, y)
        self.board_space.add(shape.getBody())
        self.board_space.add(shape.getShape())
    
    def removeShape(self, shape):
        self.board_space.remove(shape.getBody())
        self.board_space.remove(shape.getShape())
    
    def moveShape(self, shape, x, y):
        shape.position = x, y
    
    def attach(self, user):
        self.user_list.append(user)
        print("The user", user, "has been attached to the board", self)
    
    def detach(self, user):
        self.user_list.remove(user)
        print("The user", user, "has been detached from the board", self)

    @staticmethod
    def list():
        for b in Board.board_list:
            print("The board", b, "is available with the name", b.board_name)


class Shape:
    """ Shape class is a base class for other sorts of shapes. """
    # Following attributes are shared among all shapes.
    def __init__(self, body, shape):
        self.__body = body
        self.__shape = shape
        print("Following shape created: ", self.__shape)

    def getBody(self):
        return self.__body
    def getShape(self):
        return self.__shape
    def setPosition(self, x, y):
        self.__body.position = x, y

class Ball(Shape):
    """ Ball class consists of Bowling, Tennis and Marble Balls.
        Could use multiple inheritance, but looked unintuitive.  """
    
    def __init__(self, ball_type="Marble"):
        if ball_type == "Bowling":
            self.ball_moment = pymunk.moment_for_circle(30, 0, 30)
            self.ball_body = pymunk.Body(30, self.ball_moment)            
            self.ball_shape = pymunk.Circle(self.ball_body, 30)
            self.ball_shape.elasticity = 0.65
            self.ball_shape.friction = 0.34
            
        elif ball_type == "Tennis":
            self.ball_moment = pymunk.moment_for_circle(8, 0, 8)
            self.ball_body = pymunk.Body(8, self.ball_moment)            
            self.ball_shape = pymunk.Circle(self.ball_body, 8)
            self.ball_shape.elasticity = 0.728
            self.ball_shape.friction = 0.51

        elif ball_type == "Marble":
            self.ball_moment = pymunk.moment_for_circle(5, 0, 5)
            self.ball_body = pymunk.Body(1, self.ball_moment)
            self.ball_shape = pymunk.Circle(self.ball_body, 5)
            self.ball_shape.elasticity = 0.1
            self.ball_shape.friction = 0.94
        else:
            print("This shouldn't happen. Enter valid ball type!(Bowling, Tennis, Marble)")
        super().__init__(self.ball_body, self.ball_shape)



class Block(Shape):
    """ Block class consists of Domino and Book blocks.
        Could use multiple inheritance, but looked unintuitive.  """
    
    def __init__(self, block_type="Domino"):
        if block_type == "Book":
            self.block_shape = pymunk.Poly(None, ((0,0),(20,0),(20,40),(0,40)))
            self.block_moment = pymunk.moment_for_poly(15, self.block_shape.get_vertices())
            self.block_body = pymunk.Body(2, self.block_moment)            
            self.block_shape.elasticity = 0.1
            self.block_shape.friction = 0.94
            
        elif block_type == "Domino":
            self.block_shape = pymunk.Poly(None, ((0,0),(2,0),(2,4),(0,4)))
            self.block_moment = pymunk.moment_for_poly(15, self.block_shape.get_vertices())
            self.block_body = pymunk.Body(2, self.block_moment)  
            self.block_shape.elasticity = 0.2
            self.block_shape.friction = 0.51
        else:
            print("This shouldn't happen. Enter valid ball type!(Book, Domino)")
        super().__init__(self.block_body, self.block_shape)

class Segment(Shape):
    """ Segment class consists of Fixed and Rotating segments.
        Could use multiple inheritance, but looked unintuitive.  """
    
    def __init__(self, segment_type="Fixed"):
        if segment_type == "Fixed":
            self.segment_moment = pymunk.moment_for_segment(20, (75,75), (800,15), 5)
            self.segment_body = pymunk.Body(20, self.segment_moment, body_type=pymunk.Body.KINEMATIC)
            self.segment_shape = pymunk.Segment(self.segment_body, (75,75), (800,15), 5)
            self.segment_shape.elasticity = 0.1
            self.segment_shape.friction = 0.94
            
        elif segment_type == "Rotating":
            self.segment_moment = pymunk.moment_for_segment(20, (75,75), (800,15), 5)
            self.segment_body = pymunk.Body(20, self.segment_moment)
            self.segment_shape = pymunk.Segment(self.segment_body, (75,75), (800,15), 5)
            self.segment_shape.elasticity = 0.1
            self.segment_shape.friction = 0.94
        else:
            print("This shouldn't happen. Enter valid ball type!(Book, Domino)")
        super().__init__(self.segment_body, self.segment_shape)


