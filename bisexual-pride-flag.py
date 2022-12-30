# Bisexual pride procedural thinger for lumicube, written (terribly) by Nicole Roy, 2022, based on demo code from Abstract Foundry.

import colorsys

def lava_colour(x, y, z, t):
    scale = 0.10
    speed = 0.05
    hue = noise_4d(scale * x, scale * y, scale * z, speed * t)
    rgb = list(colorsys.hsv_to_rgb(hue, 1, 1))
    rgb[1] = -1
    while rgb[0] <= -1 or rgb[0] >= 1:
        if rgb[0] <=-1:
            rgb[0] += random.uniform(0.01, 0.5)
        if rgb[0] >= 1:
            rgb[0] -= random.uniform(0.01, 0.5)
    try:
        hsv = list(colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2]))
    except:
        hsv = list(colorsys.rgb_to_hsv(-0.2, 0, 1))
    hsvcol = list(colorsys.rgb_to_hsv(-0.2, 0, 1))
    try:
        hsvcol = list(colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2]))
        return hsv_colour(hsv[0], hsv[1], hsv[2])
    except:
        return hsv_colour(hsv[0], hsv[1], hsv[2])

def paint_cube(t):
    colours = {}
    for x in range(9):
        for y in range(9):
            for z in range(9):
                if x == 8 or y == 8 or z == 8:
                    colour = lava_colour(x, y, z, t)
                    colours[x,y,z] = colour
    display.set_3d(colours)

t = 0
while True:
    paint_cube(t)
    time.sleep(1/30)
    t += 1

