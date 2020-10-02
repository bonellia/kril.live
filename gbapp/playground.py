import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions

window = pyglet.window.Window(1280, 720, "Pymunk Tester", resizable=False)
options = DrawOptions()

space = pymunk.Space()
space.gravity = 0, 500

# DYNAMIC, affected by gravity and other forces (ball, player, enemies etc.)
# KINEMATIC, not affected by gravity or other forces, but can be moved programatically (platforms, doors)
# STATIC, not affected by gravity or other forces, and cannot be moved (ground, building, immovable objects)

mass = 1
radius = 30
circle_moment = pymunk.moment_for_circle(mass, 0, radius)
circle_body = pymunk.Body(mass, circle_moment)
circle_body.position = 100, 100
circle_shape = pymunk.Circle(circle_body, radius)

ceiling_moment = pymunk.moment_for_segment(mass, (0,0), (800, 0), 5)
ceiling_body = pymunk.Body(mass, ceiling_moment, body_type=pymunk.Body.KINEMATIC)
ceiling_shape = pymunk.Segment(ceiling_body, (0,0), (800, 0), 5)
ceiling_body.position = 100, 700

poly_shape = pymunk.Poly.create_box(None, size=(50,50))
poly_moment = pymunk.moment_for_poly(mass, poly_shape.get_vertices())
poly_body = pymunk.Body(mass, poly_moment)
poly_shape.body = poly_body
poly_body.position = 250, 100

segment_moment = pymunk.moment_for_segment(mass, (0,0), (0, 400), 2)
segment_body = pymunk.Body(mass, segment_moment)
segment_shape = pymunk.Segment(segment_body, (0,0), (0,400), 2)
segment_body.position = 400, 100

# Counter clock-wise
triangle_shape = pymunk.Poly(None, ((0,0), (100, 0), (50, 100)))
triangle_moment = pymunk.moment_for_poly(mass, triangle_shape.get_vertices())
triangle_body = pymunk.Body(mass, triangle_moment)
triangle_body.position = 550, 100
triangle_shape.body = triangle_body

penta_shape = pymunk.Poly(None, ((0,0), (100,0), (150, 100), (50,200), (-50, 100)))
penta_moment = pymunk.moment_for_poly(mass, penta_shape.get_vertices())
penta_body = pymunk.Body(mass, penta_moment)
penta_body.position = 750, 100
penta_shape.body = penta_body

space.add(circle_body, circle_shape, poly_body, poly_shape, segment_body, segment_shape, ceiling_body, ceiling_shape, triangle_body, triangle_shape, penta_body, penta_shape)


@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)

def update(dt):
    space.step(dt)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()