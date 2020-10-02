from goldberg import *

# Init tests.
window = pyglet.window.Window(1280, 720, "Pymunk Tester", resizable=False)
options = DrawOptions()
# Create a user.
user1 = User("Taha")
user2 = User("Artun")
# Create a board.
board1 = Board(1280, 720, "TestBoard")
# Attach both users to board1.
board1.attach(user1)
board1.attach(user2)
# Create 2 marbles.
marble1 = Ball('Bowling')
marble2 = Ball('Bowling')
# Add marbles into the board.
board1.addShape(shape=marble1, x=250, y=550)
board1.addShape(shape=marble2, x=350, y=350)
# Create a segment.
segment1 = Segment("Fixed")
# Add segment into the board.
board1.addShape(shape=segment1, x=50, y=50)
# List current boards.
Board.list()

# View the board using Pyglet
@window.event
def on_draw():
    window.clear()
    board1.board_space.debug_draw(options)

def update(dt):
    board1.board_space.step(dt)
    for shape in board1.board_space.shapes:
        if shape.body.position.y < -100:
            board1.board_space.remove(shape.body, shape)
            print(shape, "has been removed to save resources.")
            print("Current shapes in the board:", board1.board_space.shapes)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()