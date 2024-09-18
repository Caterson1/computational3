import random
from gravitational_objects import *
import pygame as p
import sys  # most commonly used to turn the interpreter off (shut down your game)
from data import *

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
    for i in object_list:
        p.draw.circle(place_to_draw_stuff, i.color, ball_xy(i), 1)


#
# def daymonthyear(time):
#     year = time /365
#     day =


# PUT SETUP CODE HERE ----------------------------------------------------------
systems = [
    System([CelestialBody(Vec(), Vec(), 1988500E24, "SUN", 696.34E3),
            CelestialBody(Vec(696.34E3 * 30), Vec(), 12000, "ASTEROID", 10)]),
    System([CelestialBody(Vec(), Vec(), 3.302e+23, "MERCURY", 2.4397E6),
            CelestialBody(Vec(2.4397E6 * 30), Vec(), 12000, "ASTEROID", 10)]),
    System([CelestialBody(Vec(), Vec(), 4.8685e+24, "VENUS", 6.0518E6),
            CelestialBody(Vec(6.0518E6 * 30), Vec(), 12000, "ASTEROID", 10)]),
    System([CelestialBody(Vec(), Vec(), 5.972190000000001e+24, "EARTH", 6.378e+6),
            CelestialBody(Vec(6.378e+6 * 30), Vec(), 12000, "ASTEROID", 10)]),
    System([CelestialBody(Vec(), Vec(), 6.417099999999999e+23, "MARS", 3390E3),
            CelestialBody(Vec(3390E3 * 30), Vec(), 12000, "ASTEROID", 10)]),
    System([CelestialBody(Vec(), Vec(), 1.89818722e+27, "JUPITER", 69911E3),
            CelestialBody(Vec(69911E3 * 30), Vec(), 12000, "ASTEROID", 10)]),
    System([CelestialBody(Vec(), Vec(), 5.6834e+26, "SATURN", 58232E3),
            CelestialBody(Vec(58232E3 * 30), Vec(), 12000, "ASTEROID", 10)]),
    System([CelestialBody(Vec(), Vec(), 1.0240900000000002e+26, "NEPTUNE", 25362E3),
            CelestialBody(Vec(25362E3 * 30), Vec(), 12000, "ASTEROID", 10)]),
    System([CelestialBody(Vec(), Vec(), 8.681300000000002e+25, "URANUS", 24.622E6),
            CelestialBody(Vec(24.622E6 * 30), Vec(), 12000, "ASTEROID", 10)])
]
for system in systems:
    for o in system.directory:
        p.draw.circle(screen, o.color, ball_xy(o), 3)
# PUT SETUP CODE HERE ----------------------------------------------------------

running = False
while True:
    clock = font.render(f'{round(timer / 3600 / 24, 3)} days', False, (255, 255, 255), (0, 0, 0))
    clockRect = clock.get_rect()
    clockRect.topleft = (10, 10)
    screen.blit(clock, clockRect)
    tracking2 = font.render(f'tracking {tracking.name.upper()}', False, (255, 255, 255), (0, 0, 0))
    trackrect = tracking2.get_rect()
    trackrect.bottomleft = (10, HEIGHT - 10)
    screen.blit(tracking2, trackrect)
    # keystroke example
    for event in p.event.get():
        if event.type == p.QUIT:  # this refers to clicking on the "x"-close
            p.quit()
            sys.exit()

        elif event.type == p.KEYUP:
            for system in systems:
                for o in system.directory:
                    p.draw.circle(screen, o.color, ball_xy(o), 3)

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

    x0 = -tracking.pos.x * scale + WIDTH / 2
    y0 = tracking.pos.y * scale + HEIGHT / 2

    if running:
        # background
        for z in range(100):

            timer += dt
            # print(timer * 1.15741e-5)
            for system in systems:
                system.step()
                if len(system.directory) > 1:
                    if system.directory[1].pos.x <= system.directory[0].r:
                        print(f"MAX VELOCITY FOR {system.directory[0].name} = {mag(system.directory[1].v)} m/s")
                        del system.directory[1]
                for o in system.directory:
                    p.draw.circle(screen, o.color, ball_xy(o), 3)
            # print(timer*1.15741e-5)
            # print(timer*1.15741e-5)

            # screen.fill((0, 0, 0))
    # p.draw.rect(screen, (50, 200, 100), (0, y0, WIDTH, HEIGHT))
    p.display.flip()

    # This sets an upper limit on the frame rate (here 100 frames per second)
    # often you won't be able
    # p.time.Clock().tick(1)
