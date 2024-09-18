import random
from gravitational_objects import *
import pygame as p
import sys  # most commonly used to turn the interpreter off (shut down your game)
from data import *
from Vec2d import *
from shapely import LineString, Point, intersects

p.font.init()

# Constants - sets the size of the window
window_bounds = WIDTH, HEIGHT, scale = 600, 600, 0.5E7 ** -1
origin = x0, y0 = WIDTH / 2, HEIGHT - HEIGHT / 2  # This is the new origin
timer = 0
font = p.font.SysFont('Monocraft', 12)
null = CelestialBody(Vec())
null.name = "null"
tracking = null
panx = 0
pany = 0


def ball_xy(ball):
    return x0 + ball.pos.x * scale + panx, y0 - ball.pos.y * scale + pany


screen = p.display.set_mode((WIDTH, HEIGHT))


def pygame_init():
    # Screen or whatever you want to call it is your best friend - it's a canvas
    # or surface where you can draw - generally you'll have one large canvas and
    # additional surfaces on top - effectively breaking things up and giving
    # you the ability to have multiples scenes in one window
    p.init()
    screen.fill((180, 210, 255))
    p.display.set_caption('Fireworks')


def drawer(object_list, place_to_draw_stuff=screen):
    p.draw.circle(screen, (0, 255, 0),
                  (x0 + system.directory[2].pos.x * scale + panx, y0 - system.directory[2].pos.y * scale + pany),
                  (checkr) * scale)
    for i in object_list:
        p.draw.circle(place_to_draw_stuff, i.color, ball_xy(i), i.r*scale)

        # p.draw.circle(place_to_draw_stuff, i.color, ball_xy(i), 5)


#
# def daymonthyear(time):
#     year = time /365
#     day =


# PUT SETUP CODE HERE ----------------------------------------------------------
system = System()
system.add(getdata("sun"))
system.add(getdata("earth"))
print("READY")
system.add(getdata(301))
system.directory[0].r = 696.34E6
system.directory[1].r = 6.371E6
system.directory[2].r = 1.74E6
rdiff = system.directory[0].r - system.directory[1].r
dtotal = minus_one_D(system.directory[1].pos - system.directory[0].pos)
distance_moon_to_earth = minus_one_D(system.directory[2].pos - system.directory[1].pos)
checkr = ((mag2d(distance_moon_to_earth) * rdiff) / mag2d(dtotal)) + system.directory[1].r
# system.directory.append(CelestialBody(Vec(-5E8)))
# PUT SETUP CODE HERE ----------------------------------------------------------

drawer(system.directory)
running = False
while True:

    # keystroke example
    for event in p.event.get():
        if event.type == p.QUIT:  # this refers to clicking on the "x"-close
            p.quit()
            sys.exit()

        elif event.type == p.KEYUP:
            drawer(system.directory)

        elif event.type == p.KEYDOWN:  # there's a separate system built in
            if event.key == p.K_SPACE:
                if running is False:
                    running = True
                    print("START")
                elif running is True:
                    running = False
                    print("PAUSE")
            if event.key == p.K_UP:
                screen.fill((0, 0, 0))
                mod = p.key.get_mods()
                if mod == p.KMOD_LSHIFT:
                    scale = scale * 10
                elif mod == p.KMOD_RSHIFT:
                    scale = scale * 100
                else:
                    scale = scale * 2

            if event.key == p.K_DOWN:
                screen.fill((0, 0, 0))
                mod = p.key.get_mods()
                if mod == p.KMOD_LSHIFT:
                    scale = scale / 10
                elif mod == p.KMOD_RSHIFT:
                    scale = scale / 100
                else:
                    scale = scale / 2
                drawer(system.directory)
            if p.K_1 <= event.key <= p.K_9:
                panx = 0
                pany = 0
                print(event.key, p.K_1)
                starter = event.key - p.K_1
                # mod = p.key.get_mods()
                # if mod == p.KMOD_LSHIFT or p.KMOD_RSHIFT:
                #     starter += 9
                # if mod == p.KMOD_LCTRL or p.KMOD_RCTRL:
                #     starter += 18
                try:
                    tracking = system.directory[starter]
                except IndexError:
                    tracking = system.directory[0]
                else:
                    tracking = system.directory[starter]
                print(starter)
            if event.key == p.K_r:
                tracking = null
                panx = 0
                pany = 0
            if event.key == p.K_w:
                dpan = 1
                mod = p.key.get_mods()
                if mod == p.KMOD_LSHIFT:
                    dpan = 5
                elif mod == p.KMOD_RSHIFT:
                    dpan = 10
                pany -= dpan
            if event.key == p.K_s:
                dpan = 1
                mod = p.key.get_mods()
                if mod == p.KMOD_LSHIFT:
                    dpan = 5
                elif mod == p.KMOD_RSHIFT:
                    dpan = 10
                pany += dpan
            if event.key == p.K_a:
                dpan = 1
                mod = p.key.get_mods()
                if mod == p.KMOD_LSHIFT:
                    dpan = 5
                elif mod == p.KMOD_RSHIFT:
                    dpan = 10
                panx -= dpan
            if event.key == p.K_d:
                dpan = 1
                mod = p.key.get_mods()
                if mod == p.KMOD_LSHIFT:
                    dpan = 5
                elif mod == p.KMOD_RSHIFT:
                    dpan = 10
                panx += dpan


    if running:
        # background
        for z in range(100):
            screen.fill((0,0,0))
            clock = font.render(f'{round(timer / 3600 / 24, 3)} days', False, (255, 255, 255), (0, 0, 0))
            clockRect = clock.get_rect()
            clockRect.topleft = (10, 10)
            screen.blit(clock, clockRect)
            tracking2 = font.render(f'tracking {tracking.name.upper()}', False, (255, 255, 255), (0, 0, 0))
            trackrect = tracking2.get_rect()
            trackrect.bottomleft = (10, HEIGHT - 10)
            screen.blit(tracking2, trackrect)
            x0 = -tracking.pos.x * scale + WIDTH / 2
            y0 = tracking.pos.y * scale + HEIGHT / 2
            timer += dt
            # print(timer * 1.15741e-5)
            dtotal = minus_one_D(system.directory[1].pos - system.directory[0].pos)
            distance_moon_to_earth = minus_one_D(system.directory[2].pos - system.directory[1].pos)
            checkr = ((mag2d(distance_moon_to_earth) * rdiff) / mag2d(dtotal)) \
                     + system.directory[1].r + system.directory[2].r
            system.step()
            # print(timer*1.15741e-5)
            # print(timer*1.15741e-5)
            #CHECK X-Y PLANE
            if intersects(Point(system.directory[2].pos.x, system.directory[2].pos.y).buffer(checkr).boundary,
                                  LineString([[system.directory[0].pos.x, system.directory[0].pos.y],
                                                      [system.directory[1].pos.x, system.directory[1].pos.y]])):
                if system.directory[1].pos.z - checkr < system.directory[2].pos.z < system.directory[1].pos.z + checkr:
                    print(f"eclipse at time {timer}")
            # diameter at distance from earth = earthdiam + (disfromearth(difference in diam))/totaldis
            drawer(system.directory)
            p.draw.line(screen, (255, 255, 255), ball_xy(system.directory[0]), ball_xy(system.directory[1]))
            # screen.fill((0, 0, 0))    # p.draw.rect(screen, (50, 200, 100), (0, y0, WIDTH, HEIGHT))

    p.display.flip()

    # This sets an upper limit on the frame rate (here 100 frames per second)
    # often you won't be able
    # p.time.Clock().tick(1)
