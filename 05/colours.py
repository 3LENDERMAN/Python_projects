from ib111 import week_05  # noqa

# Color is represented by triple RGB (red,green,blue) in interval 0-255
# Function <nearest_colour> returns colour from dictionary that is closest to <colour> 
# parameter, if there are more colors in the same distance, return them all
#
# Proximity of colors will be measured by Manhattan distance,
# sum of absolute values of A - B so of cords. Example:
#
#     A = (150, 0, 65)
#     B = (120, 30, 100)
#
# Manhattan distance equales
#
#    |150 - 120| + |0 - 30| + |65 - 100| = 30 + 30 + 35 = 95


Colour = tuple[int, int, int]


def nearest_colour(names: dict[str, Colour],
                   colour: Colour) -> set[str]:
    closest_colors: set[str] = set()
    col_name: str = ""
    red,green,blue = colour
    dist: int = 1000
    for name, (r,g,b) in names.items():
        x = (abs(r - red) + abs(g - green) + abs(b - blue))
        if x < dist:
            dist = x
            col_name = name

    closest_colors.add(col_name)
    for name, (r,g,b) in names.items():
        x = (abs(r - red) + abs(g - green) + abs(b - blue))
        if x == dist:
            col_name = name
            closest_colors.add(col_name)
    return closest_colors


def main() -> None: # run tests
    names = {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'purple': (128, 0, 128),
        'cyan': (0, 255, 255),
        'magenta': (255, 0, 255),
        'lime': (50, 205, 50),
        'pink': (255, 192, 203),
        'teal': (0, 128, 128),
        'lavender': (230, 230, 250),
        'maroon': (128, 0, 0),
        'navy': (0, 0, 128),
        'olive': (128, 128, 0),
        'silver': (192, 192, 192),
        'grey': (128, 128, 128),
        'orange': (255, 165, 0),
        'brown': (165, 42, 42),
        'fuchsia': (255, 0, 255),
        'violet': (238, 130, 238),
        'indigo': (75, 0, 130),
        'gold': (255, 215, 0),
        'peachpuff': (255, 218, 185),
        'darkorange': (255, 140, 0),
        'chartreuse': (127, 255, 0),
        'lightpink': (255, 182, 193),
        'skyblue': (135, 206, 235),
        'darkgreen': (0, 100, 0),
    }

    rgb = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255)
    }

    assert nearest_colour(names, (1, 1, 1)) == {'black'}
    assert nearest_colour(names, (254, 254, 254)) == {'white'}
    assert nearest_colour(rgb, (1, 1, 1)) == \
        {'red', 'green', 'blue'}


if __name__ == "__main__":
    main()
